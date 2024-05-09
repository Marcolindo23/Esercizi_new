#Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione. 
#L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere.
#La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni che sono soddisfatte.
def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA or conditionB and conditionC == True:
        return "Operazione permessa"
    else:
        return "Operazione negata"
conditionA= bool(input("La condizione A è:"))
conditionB= bool(input("La condizione B è:"))
conditionC= bool(input("La condizione C è:"))
Risultato=check_combination(conditionA, conditionB, conditionC)
print(Risultato)


#Scrivi una funzione che accetti tre parametri: username, password e status di attivazione dell'account (attivo/non attivo). 
#L'accesso è consentito solo se il nome utente è "admin", 
#la password corrisponde a "12345" e l'account è attivo. La funzione ritorna "Accesso consentito" oppure "Accesso negato".
def check_access(username: str, password: ..., is_active: bool) -> str:
    if username=="admin" and password=="12345" and is_active==True:
        return "Accesso consentito"
    else:
        return "Accesso negato"
username= str(input("L'username della personaè:"))
password= str(input("La password della personaè:"))
is_active= bool(input("Lo status di attivazione è: "))
Risultato1=check_access(username, password, is_active)
print(Risultato1)


#Scrivi una funzione che calcola la media di una lista di numeri e ritorna il valore arrotondato all'intero più vicino.
def rounded_average(numbers: list[int]) -> int:
    media= sum(numbers)/len(numbers)
    x=round(media)
    return x


#Scrivi una funzione che ritorna il valore massimo, minimo e la media di una lista di numeri interi.
def list_statistics(numbers: list[int]) -> ... :
    valore_massimo=max(numbers)
    valore_minimo=min(numbers)
    media1=sum(numbers)/len(numbers)
    return valore_massimo, valore_minimo, media1


#Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, 
#cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.
def check_parentheses(expression: str) -> bool:
    count: int=0
    for elem in expression:
        if elem == "(":
            count+=1
        elif elem == ")":
            count -= 1
        if count < 0:
            return False
        return count == 0


#Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi.
#Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.




    

