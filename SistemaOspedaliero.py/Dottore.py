from Persona import Persona

class Dottore(Persona):
    
    def __init__(self, first_name: str, last_name: str, specialization: str, parcel: float):
        super().__init__(first_name, last_name)

        self.__specialization = specialization
        self.__parcel = parcel

        if type(specialization) == str:
            self.__specialization = specialization
        
        if type(parcel) == float:
            self.__parcel = parcel

        if type(specialization) != str:
            self.__specialization = None
            print( "La specializzazione inserita non è una stringa!")
        
        if type(parcel) != float:
            self.__parcel = None
            print( "La parcella inserita non è un float!")
        
    def setSpecialization(self, specialization : str):
        if type(specialization) == str:
            self.__specialization = specialization
        else:
            print("La specializzazione inserita non è una stringa!")
    
    def setParcel(self, parcel : float):
        if type(parcel) == float:
            self.__parcel = parcel
        else:
            print("La parcella inserita non è un float!")
    
    def getSpecialization(self):
        return self.__specialization
    
    def getParcel(self):
        return self.__parcel
    
    def isAValidDoctor(self):
        if self.getAge() > 30:
            print(f"The Doctor {self.getName()} {self.getLastName()} is valid")
        else:
            print(f"The Doctor {self.getName()} {self.getLastName()} is not valid")

    
    def doctorGreet(self):
        print(self.greet() + f" e sono un {self.__specialization}!")
        
dottore1 = Dottore(first_name = "Felice", last_name = "Mastronzo", specialization = "Neurologo", parcel = 2000.36)
dottore1.set_Age(45)
dottore1.isAValidDoctor()
dottore1.doctorGreet()
            


    
