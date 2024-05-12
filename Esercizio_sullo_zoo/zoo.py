#Creaiamo un sistema di gestione di uno zoo virtuale

#Sistema di gestione dello zoo virtuale

#Classi:

#1. Zoo: questa classe rappresenta uno zoo. Lo zoo ha dei recinti fences e dei guardiani dello zoo, zoo_keepers.

#2. Animal: questa classe rappresenta un animale nello zoo. Ogni animale ha questi attributi: name, species, age, height, width, preferred_habitat, health che è uguale a round(100 * (1 / age), 3).

#3. Fence: questa classe rappresenta un recinto dello zoo in cui sono tenuti gli animali. I recinti possono contenere uno o più animali. I recinti possono hanno gli attributi area, temperature e habitat.

#4. ZooKeeper: questa classe rappresenta un guardiano dello zoo responsabile della gestione dello zoo. I guardiani dello zoo hanno un name, un surname, e un id. Essi possono nutrire gli animali, pulire i recinti e svolgere altri compiti nel nostro zoo virtuale.

#Funzionalità:

#1. add_animal(animal: Animal, fence: Fence) (Aggiungi nuovo animale): consente al guardiano dello zoo di aggiungere un nuovo animale allo zoo. L'animale deve essere collocato in un recinto adeguato in base alle esigenze del suo habitat e se c'è ancora spazio nel recinto, ovvero se l'area del recinto è ancora sufficiente per ospitare questo animale.

#2. remove_animal(animal: Animal, fence: Fence) (Rimuovi animale): consente al guardiano dello zoo di rimuovere un animale dallo zoo. L'animale deve essere allontanato dal suo recinto. Nota bene: L'area del recinto deve essere ripristinata dello spazio che l'animale rimosso occupava.

#3. feed(animal: Animal) (Dai da mangiare agli animali): implementa un metodo che consenta al guardiano dello zoo di nutrire tutti gli animali dello zoo. Ogni volta che un animale viene nutrito, la sua salute incrementa di 1% rispetto alla sua salute corrente, ma le dimensioni dell'animale (height e width) vengono incrementate del 2%. Perciò, l'animale si può nutrire soltanto se il recinto ha ancora spazio a sufficienza per ospitare l'animale ingrandito dal cibo.

#4. clean(fence: Fence) (Pulizia dei recinti): implementare un metodo che consenta al guardiano dello zoo di pulire tutti i recinti dello zoo. Questo metodo restituisce un valore di tipo float che indica il tempo che il guardiano impiega per pulire il recinto. Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto. Se l'area residua è pari a 0, restituire l'area occupata.

#5. describe_zoo() (Visualizza informazioni sullo zoo): visualizza informazioni su tutti i guardani dello zoo, sui recinti dello zoo che contengono animali. 


class Zoo:
    def __init__(self):
        # Inizializza una lista per i recinti e una lista per i guardiani dello zoo
        self.fences = []
        self.zoo_keepers = []

    def add_fence(self, fence):
        # Aggiunge un recinto alla lista dei recinti dello zoo
        self.fences.append(fence)

    def add_zoo_keeper(self, zoo_keeper):
        # Aggiunge un guardiano alla lista dei guardiani dello zoo
        self.zoo_keepers.append(zoo_keeper)

    def add_animal(self, animal, fence):
        # Aggiunge un animale al recinto specificato se c'è spazio sufficiente
        if fence in self.fences and fence.area >= animal.height * animal.width:
            fence.add_animal(animal)
            return True
        else:
            return False

    def remove_animal(self, animal, fence):
        # Rimuove un animale dal recinto specificato
        if fence in self.fences and animal in fence.animals:
            fence.remove_animal(animal)
            return True
        else:
            return False

    def feed(self, animal):
        # Nutre un animale, aumentando la sua salute e le sue dimensioni
        animal.health += 1
        animal.height *= 1.02
        animal.width *= 1.02

    def clean(self, fence):
        # Calcola il tempo necessario per pulire un recinto in base all'area occupata dagli animali
        occupied_area = sum(animal.height * animal.width for animal in fence.animals)
        if fence.area - occupied_area > 0:
            return occupied_area / (fence.area - occupied_area)
        else:
            return occupied_area

    def describe_zoo(self):
        print("Guardians:")
        for zoo_keeper in self.zoo_keepers:
            print(f"ZooKeeper(name={zoo_keeper.name}, surname={zoo_keeper.surname}, id={zoo_keeper.id})")

        print("\nFences:")
        for fence in self.fences:
            print(f"Fence(area={fence.area}, temperature={fence.temperature}, habitat={fence.habitat})")
            if fence.animals:  # Verifica se ci sono animali nel recinto
                print("\nwith animals:")
                for animal in fence.animals:
                    print(f"Animal(name={animal.name}, species={animal.species}, age={animal.age})")
            else:
                print("No animals")
            print("#" * 30)  # Separatore tra recinti
class Animal:
    def __init__(self, name, species, age, height, width, preferred_habitat):
        # Inizializza un animale con i relativi attributi
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        # Calcola la salute dell'animale in base all'età
        self.health = round(100 * (1 / age), 3)

class Fence:
    def __init__(self, area, temperature, habitat):
        # Inizializza un recinto con i relativi attributi e una lista vuota di animali
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals = []

    def add_animal(self, animal):
        # Aggiunge un animale al recinto
        self.animals.append(animal)

    def remove_animal(self, animal):
        # Rimuove un animale dal recinto
        self.animals.remove(animal)

class ZooKeeper:
    def __init__(self, name, surname, id):
        # Inizializza un guardiano dello zoo con i relativi attributi
        self.name = name
        self.surname = surname
        self.id = id
lorenzo_maggi = ZooKeeper(name="Lorenzo", surname="Maggi", id=1234)
fence = Fence(area=100, temperature=25, habitat="Continentale")
scoiattolo = Animal(name="Scoiattolo", species="Blabla", age=25, height=10, width=5, preferred_habitat="Alberi")
lupo = Animal(name="Lupo", species="Lupus", age=14, height=20, width=15, preferred_habitat="Foresta")
# Aggiunta degli animali al recinto
fence.add_animal(scoiattolo)
fence.add_animal(lupo)

# Creazione dello zoo e aggiunta dei recinti e dei guardiani
zoo = Zoo()
zoo.add_fence(fence)
zoo.add_zoo_keeper(lorenzo_maggi)

# Descrizione dello zoo
zoo.describe_zoo()