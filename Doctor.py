class Doctor:
    """A class that deals with the Doctor operations"""

    def __init__(self, first_name, surname, speciality):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            speciality (string): Doctor`s speciality
        """

        self.__first_name = first_name
        self.__surname = surname
        self.__speciality = speciality
        self.__patients = []
        self.__appointments = []

    def full_name(self):
        return self.__first_name + " " + self.__surname

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_surname(self):
        return self.__surname

    def set_surname(self, surname):
        self.__surname = surname

    def get_speciality(self):
        return self.__speciality

    def set_speciality(self, speciality):
        self.__speciality = speciality

    def add_patient(self, patient):
        self.__patients.append(patient)

    def __str__(self):
        return f'{self.full_name():^30}|{self.__speciality:^15}'
