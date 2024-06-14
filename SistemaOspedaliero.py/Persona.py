class Persona:
    def __init__(self, first_name: str, last_name: str):
        self.__first_name = first_name
        self.__last_name = last_name

        if type(first_name) != str:
            self.__first_name = None
            print("Il nome inserito non è una stringa!")
        
        if type(last_name) != str:
            self.__last_name = None
            print("Il cognome inserito non è una stringa!")
        
        if type(first_name) and type(last_name) == str:
            self.__age = 0
        
        if type(first_name) and type(last_name) != str:
            self.__age = None
    
    def setName(self, first_name: str):
        if type(first_name) == str:
            self.__first_name = first_name

        else:
            print("Il nome inserito non è una stringa!")
    
    def setLastName(self, last_name: str):
        if type(last_name) == str:
            self.__last_name = last_name

        else:
            print("Il nome inserito non è una stringa!")
    
    def set_Age(self, age: int):
        if type(age) == int:
            self.__age = age

        else:
            print("L'età deve essere un numero intero!")
    
    def getName(self):
        return self.__first_name
    
    def getLastName(self):
        return self.__last_name
    
    def getAge(self):
        return self.__age
    
    def greet(self):
        return f"Ciao sono {self.__first_name} {self.__last_name}, Ho {self.__age} anni"

persona1 = Persona(first_name = "Felice", last_name = "Mastronzo")
persona1.set_Age(29)
persona1.greet()
    

    

    


        


        
