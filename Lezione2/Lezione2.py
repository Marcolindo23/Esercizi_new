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
Invitati=["Rafael Nadal", "Elon Musk", "Cristiano Ronaldo"]
message3: str="vorresti venire a cena a casa mia?"
for c in Invitati:
    print(f"Good evening {c} would you like to come to my house for dinner this evening?")
#3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations.
#You’ll have to think of someone else to invite.
#• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
#• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#• Print a second set of invitation messages, one for each person who is still in your list.
print(f"{Invitati[1]} non potrà venire sta sera a cena questa perchè aveva da fare")





