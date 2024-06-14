from Persona import Persona

class Paziente(Persona):
    def __init__(self, first_name: str, last_name: str, ID: str):
        super().__init__(first_name, last_name)

        self.__ID = ID
    
    def setIDCode(self, ID):
        self.__ID = ID
    
    def getIDCode(self):
        return self.__ID

    def patientInfo(self):
        print(f"Paziente: {self.getName()} {self.getLastName()}\nID: {self.getIDCode()}")


paziente = Paziente("Mario", "Rossi", "12345")
paziente.patientInfo()