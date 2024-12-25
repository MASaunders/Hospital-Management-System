from Doctor import Doctor


class Admin:
    """A class that deals with the Admin operations"""

    def __init__(self, username, password, address=''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address = address

    def view(self, a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index + 1:3}|{item}')

    def login(self):
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """

        print("-----Login-----")
        # Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # check if the username and password match the registered ones
        if username == 'admin' and password == '123':
            print("Logged in as admin.")
            return True

    def find_index(self, index, doctors):
        # check that the doctor id exists
        if index in range(0, len(doctors)):
            return True

        # if the id is not in the list of doctors
        else:
            return False

    def get_doctor_details(self):
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and speciality of the doctor in that order.
        """
        first_name = input("Enter first name: ")
        surname = input("Enter surname: ")
        speciality = input("enter speciality: ")

        return first_name, surname, speciality

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")
        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        while True:
            op = input("Select Operation: ")

            # register
            if op == '1':
                print("-----Register-----")

                # get the doctor details
                print('Enter the doctor\'s details:')
                first_name, surname, speciality = self.get_doctor_details()

                # check if the name is already registered
                name_exists = False
                for doctor in doctors:
                    if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                        print('Name already exists.')
                        return True
                    elif first_name != doctor.get_first_name() and surname != doctor.get_surname():
                        name_exists = False

                    else:
                        print("Invalid operation")
                        break  # save time and end the loop

                if name_exists == False:
                    doctors.append(Doctor(first_name, surname, speciality))
                    # add the doctor to the list of doctors
                    print('Doctor registered.')
                    return

            # View
            elif op == '2':
                print("-----List of Doctors-----")
                print('ID |          Full name           |  Speciality')
                return self.view(doctors)

            # Update
            elif op == '3':
                while True:
                    print("-----Update Doctor`s Details-----")
                    print('ID |          Full name           |  Speciality')
                    self.view(doctors)
                    try:
                        index = int(input('Enter the ID of the doctor: ')) - 1
                        doctor_index = self.find_index(index, doctors)

                        if doctor_index != False:
                            break

                        else:
                            print("Doctor not found.")

                            # doctor_index is the ID mines one (-1)

                    except ValueError:  # the entered id could not be changed into an int
                        print('The ID entered is incorrect')

                # menu
                print('Choose the field to be updated:')
                print(' 1 First name')
                print(' 2 Surname')
                print(' 3 Speciality')
                op = input('Input: ')  # make the user input lowercase

                if op == '1':
                    first_name = input("Update first name: ")
                    doctors[index].set_first_name(first_name)
                    print("First name updated successfully.")
                    return

                elif op == '2':
                    surname = input("Update surname: ")
                    doctors[index].set_surname(surname)
                    print("Surname updated successfully.")
                    return

                elif op == '3':
                    speciality = input("Update speciality: ")
                    doctors[index].set_speciality(speciality)
                    print("Speciality updated successfully.")
                    return

                else:
                    print("Invalid operation")
                    break

            # Delete
            elif op == '4':
                print("-----Delete Doctor-----")
                print('ID |          Full Name           |  Speciality')
                self.view(doctors)

                doctor_index = input('Enter the ID of the doctor to be deleted: ')
                try:
                    doctor_index = int(doctor_index) - 1

                    if doctor_index in range(len(doctors)):
                        doctors.pop(int(doctor_index))
                        print("\nDoctor removed from the system successfully.")
                        break

                    else:
                        print("ID out of range")
                        break

                except ValueError:
                    print("ID out of range")
                    return

            # if the id is not in the list of patients
            else:
                print('Invalid operation chosen. Check your spelling!')

    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |      Symptoms ')
        return self.view(patients)

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |      Symptoms ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) - 1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return  # stop the procedures

        except ValueError:  # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return  # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID minus one (-1)
            doctor_index = int(doctor_index) - 1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index, doctors) != False:
                # link the patients to the doctor and vice versa
                patients[patient_index].link(doctors[doctor_index].full_name())

                print('The patient is now assign to the doctor.')
                return True

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError:  # the entered id could not be changed into an in
            print('The id entered is incorrect')

    def discharge(self, patients, discharged_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")

        index = int(input('Please enter the patient ID: '))
        discharged_patient = patients.pop(index)
        discharged_patients.append(discharged_patient)
        print("Patient discharged.")
        return

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        return self.view(discharged_patients)

    def update_details(self):
        # Allows the user to update and change username, password and address
        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')

        op = int(input('Input: '))

        if op == 1:
            try:
                username = input("Enter the new username: ")
                # Validate the username
                validate_username = input("Enter the new username again: ")
                # check if the usernames match
                if username == validate_username:
                    self.__username = username
                    print("Username updated.")

                elif username != validate_username:
                    print("Username does not match!")
            except ValueError:
                print("New username does not match!")

        elif op == 2:
            try:
                password = input('Enter the new password: ')
                # validate the password
                validate_password = input('Enter the new password again: ')
                # check if the passwords match
                if password == validate_password:
                    self.__password = password
                    print("Password updated.")
                elif password != validate_password:
                    print("Password does not match!")

            except ValueError:
                print("New password does not match")

        elif op == 3:
            address = input("Enter the address: ")
            self.__address = address
            print("Address updated.")

        else:
            print("Invalid choice.")
