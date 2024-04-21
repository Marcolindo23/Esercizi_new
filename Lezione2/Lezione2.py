# Marco Giusepponi
# 18/04/2024

print("Hello World!")

#2-3. Personal Message Use a variable to represent a person’s name, and print a message to that person.
#Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
name: str= "Ambrogio"
print(f"Ciao, {name} come stai?")
#2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.
print(name.upper())
print(name.lower())
print(name.title())
#2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. 
#Your output should look something like the following, including the quotation marks: 
#Albert Einstein once said, “A person who never made a mistake never tried anything new.”
name1: str="Albert Einstein"
message: str=  '"A person who never made a mistake never tried anything new"'
print(f"{name1}, una volta disse, {message}")
#2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). 
#Assign the value 'python_notes.txt' to a variable called filename.
#Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.
filename: str= 'python_notes.txt'
print(filename.removesuffix(".txt"))
#3-1. Names: Store the names of a few of your friends in a list called names.
#Print each person’s name by accessing each element in the list, one at a time.
names=["Edoardo", "Flavio"]
print(f"{names[0]}")
print(f"{names[-1]}")
#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them.
#The text of each message should be the same, but each message should be personalized with the person’s name.
message: str= "come stai?"
print(f"Ciao {names[0]} {message}")
print(f"Ciao {names[-1]} {message}")
#3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. 
#Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
Transportation=["Ferrari", "Autobus"]
print(f"Il mio sogno sarebbe guidare una", Transportation[0], "un giorno")
print(f"Per venire a lezione uso l'", Transportation[-1])
#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, 
#who would you invite? Make a list that includes at least three people you’d like to invite to dinner. 
#Then use your list to print a message to each person, inviting them to dinner.
Invitati=["Edoardo", "Vincenzo", "Flavio"]
message3: str="vorresti venire questa sera a cena fuori?"
for c in Invitati:
    print(f"Buonasera {c} {message}")
#3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations.
#You’ll have to think of someone else to invite.
#• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
#• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#• Print a second set of invitation messages, one for each person who is still in your list.
print(f"{Invitati[1]} non potrà venire sta sera a cena questa perchè aveva da fare")
Invitati[1]= "Noel"
print(Invitati)
for c in Invitati:
    print(f"Buonasera {c} {message}")
#3-6 More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
#• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
#• Use insert() to add one new guest to the beginning of your list.
#• Use insert() to add one new guest to the middle of your list.
#• Use append() to add one new guest to the end of your list.
#• Print a new set of invitation messages, one for each person in your list.
Invitati.insert(0, "David")
Invitati.insert(2, "Eva")
Invitati.append("Frank")
print(Invitati)
for c in Invitati:
    print(f"Buonasera {c} {message}")
#3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
#• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
#• Use pop() to remove guests from your list one at a time until only two names remain in your list.
#Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#• Print a message to each of the two people still on your list, letting them know they’re still invited.
#• Use del to remove the last two names from your list, so you have an empty list.
#Print your list to make sure you actually have an empty list at the end of your program.
message6: str="Mi dispiace ma potro invitare soltanto due persone"
persona_rimossa= Invitati.pop(0)
persona_rimossa1= Invitati.pop(1)
persona_rimossa2= Invitati.pop(3)
persona_rimossa3= Invitati.pop(0)
print(Invitati)
print(f"{persona_rimossa} {message6}")
print(f"{persona_rimossa1} {message6}")
print(f"{persona_rimossa2} {message6}")
print(f"{persona_rimossa3} {message6}")
#3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
#• Store the locations in a list. Make sure the list is not in alphabetical order.
#• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
#• Use sorted() to print your list in alphabetical order without modifying the actual list.
#• Show that your list is still in its original order by printing it.
#• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
#• Show that your list is still in its original order by printing it again.
#• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
#• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
#• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
#• Use sort() to change your list so it’s stored in reverse-alphabetical order.
#Print the list to show that its order has changed.
Posti_da_Visitare=["Stati Uniti D'America", "Lapponia", "Petra", "Machu Picchu", "India"]
print(f"La lista originale é: {Posti_da_Visitare}")
print(f"La lista in ordine alfabetico è: {sorted(Posti_da_Visitare)}")
print(f"Lista in ordine alfabetico inverso: {sorted(Posti_da_Visitare, reverse=True)}")
print(f"La lista originale é: {Posti_da_Visitare}")
Posti_da_Visitare.reverse()
print(f"Lista dopo l'inversione dell'ordine: {Posti_da_Visitare}")
Posti_da_Visitare.reverse()
print(f"Lista ripristinata all'ordine originale: {Posti_da_Visitare}")
Posti_da_Visitare.sort()
print(f"Lista ordinata in ordine alfabetico: {Posti_da_Visitare}")
Posti_da_Visitare.sort(reverse=True)
print(f"Lista ordinata in ordine alfabetico inverso: {Posti_da_Visitare}")
#3-9. Dinner Guests: Working with one of the programs from Exercises 3
#use len() to print a message indicating the number of people you’re inviting to dinner.
numero_invitati=len(Invitati)
print(F"Gli invitati a cena sono: {numero_invitati}")
#3-10. Every Function: Think of things you could store in a list. 
#For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
#Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
elementi = ["Montagne", "Fiumi", "Paesi", "Città", "Lingue"]
print(f"Lista originale: {elementi}")
elementi.append("Oceani")
print(f"Lista dopo l'aggiunta di 'Oceani': {elementi}")
elementi.insert(2, "Laghi")
print(f"Lista dopo l'inserimento di 'Laghi' alla posizione 2: {elementi}")
elementi.remove("Paesi")
print(f"Lista dopo la rimozione di 'Paesi': {elementi}")
elemento_rimosso = elementi.pop()
print(f"Ultimo elemento rimosso dalla lista: {elementi}")
print(f"Lista dopo la rimozione dell'ultimo elemento: {elementi}")
elementi.sort()
print(f"Lista ordinata in ordine alfabetico: {elementi}")
elementi.sort(reverse=True)
print(f"Lista ordinata in ordine alfabetico inverso: {elementi}")
elementi.reverse()
print(f"Lista con l'ordine degli elementi invertito: {elementi} ")
lunghezza_lista = len(elementi)
print(f"La lunghezza della lista è: {elementi}")
#6-1. Person: Use a dictionary to store information about a person you know. 
#Store their first name, last name, age, and the city in which they live. 
#You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.
persona = {"first_name": "Marco", "last_name": "Rossi", "age": 30, "city": "Roma"}
print(f"Nome: {persona['first_name']}")
print(f"Cognome: {persona['last_name']}")
print(f"Età: {persona['age']}")
print(f"Città: {persona['city']}")
#6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.Think of five names,and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. 
#Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.
numeri_preferiti = {"Marco": 7, "Anna": 12, "Luca": 5, "Giulia": 9, "Matteo": 3}
for persona, numero in numeri_preferiti.items():
    print(f"{persona} ha come numero preferito il {numero}.")
#6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
#• Think of five programming words you’ve learned about in the previous chapters. 
#Use these words as the keys in your glossary, and store their meanings as values.
#• Print each word and its meaning as neatly formatted output. 
#You might print the word followed by a colon and then its meaning, or print the word on one line 
#and then print its meaning indented on a second line. 
#Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
glossario = {
    "Variabile": "Un nome che fa riferimento a un valore memorizzato in memoria.",
    "Lista": "Una struttura dati ordinata che può contenere elementi di diversi tipi.",
    "Ciclo": "Un costrutto che permette di ripetere un blocco di istruzioni più volte.",
    "Funzione": "Un blocco di codice riutilizzabile che esegue una specifica operazione.",
    "Condizione": "Un'istruzione che permette di eseguire blocchi di codice solo se una determinata condizione è vera."
}
for parola, significato in glossario.items():
    print(f"{parola}:\n{significato}\n")
#6-7. People: Start with the program you wrote for Exercise 6-1.
#Make two new dictionaries representing different people, and store all three dictionaries in a list called people. 
#Loop through your list of people. 
#As you loop through the list, print everything you know about each person.
persona1 = { "nome": "Marco", "cognome": "Rossi", "età": 30, "città": "Roma"}
persona2 = {"nome": "Anna", "cognome": "Bianchi", "età": 25, "città": "Milano"}
persona3 = {"nome": "Luca", "cognome": "Verdi", "età": 35, "città": "Napoli"}
people = [persona1, persona2, persona3]
for persona in people:
    print(f"Nome: {persona['nome']}")
    print(f"Cognome: {persona['cognome']}")
    print(f"Età: {persona['età']}")
    print(f"Città: {persona['città']}")
    print()
#6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. 
#In each dictionary, include the kind of animal and the owner’s name. 
#Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet. 
pet1 = {"animale": "Cane", "proprietario": "Mario"}
pet2 = {"animale": "Gatto", "proprietario": "Anna"}
pet3 = {"animale": "Pappagallo", "proprietario": "Luca"}
pets = [pet1, pet2, pet3]
for pet in pets:
    print(f"Tipo di animale: {pet['animale']}")
    print(f"Proprietario: {pet['proprietario']}")
    print()
#6-9. Favorite Places: Make a dictionary called favorite_places. 
#Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. 
#To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. 
#Loop through the dictionary, and print each person’s name and their favorite places.
Posti_Preferiti = {
    "Marco": ["Roma", "Firenze", "New York"],
    "Anna": ["Parigi", "Barcellona"],
    "Luca": ["Tokyo"]
}

# Itera attraverso il dizionario dei luoghi preferiti e stampa i nomi delle persone e i loro luoghi preferiti
for persona, luoghi in Posti_Preferiti.items():
    print(f"{persona} preferisce i seguenti luoghi:")
    for luogo in luoghi:
        print(f"- {luogo}")
    print()
#6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. 
#Then print each person’s name along with their favorite numbers.
numeri_preferiti = {
    "Marco": [7, 11, 22],
    "Anna": [12, 5],
    "Luca": [9, 3, 8],
    "Giulia": [4]
}
for persona, numeri in numeri_preferiti.items():
    print(f"{persona} ha come numeri preferiti:")
    for numero in numeri:
        print(numero)
    print()  
#6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary.
#Create a dictionary of information about each city and include the country that the city is in, its approximate population, 
#and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. 
#Print the name of each city and all of the information you have stored about it.
cities = {
    "Roma": {"country": "Italia", "population": 2873000, "fact": "È la capitale d'Italia e la città più grande del paese."},
    "Parigi": {"country": "Francia", "population": 2148000, "fact": "È famosa per la sua torre Eiffel e la sua arte."},
    "Tokyo": {"country": "Giappone", "population": 13960000, "fact": "È una delle città più grandi e affollate del mondo."}
}
for city, info in cities.items():
    print(f"Informazioni su {city}:")
    for key, value in info.items():
        if key == "population":
            value = "{:,}".format(value).replace(",",".")
        print(f"{key.title()}: {value}")
    print()




