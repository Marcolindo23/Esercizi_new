#1. School Grading System:
#Create a function that takes a student's name and their scores in different subjects as input.
#The function calculates the average score and prints the student's name, average, and a message indicating whether the student passed the exam (average >= 60) or failed.
#Create a for loop to iterate over a list of students and scores, calling the function for each student.
def calcola_voto(nome, voti):
    # Calcola la media dei voti
    media_voti = sum(voti) / len(voti)
    
    # Determina se lo studente ha superato o non superato l'esame
    if media_voti >= 60:
        risultato = "Passato"
    else:
        risultato = "Non passato"
    
    # Stampa il nome dello studente, la media dei voti e il risultato
    print(f"Studente: {nome}, Media Voti: {media_voti}, Risultato: {risultato}")

# Lista degli studenti e dei loro voti
studenti = [
    {"nome": "Alice", "voti": [85, 90, 78, 92, 88]},
    {"nome": "Bob", "voti": [56, 67, 72, 65, 60]},
    {"nome": "Charlie", "voti": [45, 50, 48, 52, 55]}
]

# Itera su ogni studente e calcola il suo voto
for studente in studenti:
    calcola_voto(studente["nome"], studente["voti"])

#2. Guess the Number Game:
#Create a function that generates a random number within a range specified by the user.
#Prompt the user to guess the number within a specified maximum number of attempts.
#Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.
#Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.
import random

def gioco_indovina_numero(inizio, fine, tentativi_massimi):
    # Genera un numero casuale compreso nell'intervallo specificato dall'utente
    numero_da_indovinare = random.randint(inizio, fine)
    tentativi_fatti = 0
    
    # Stampa un messaggio per indicare il range di numeri
    print(f"Indovina un numero compreso tra {inizio} e {fine}.")

    # Ciclo che continua finché l'utente non indovina il numero o finché esaurisce i tentativi
    while tentativi_fatti < tentativi_massimi:
        # Chiede all'utente di fare un tentativo
        guess = int(input("Tentativo: "))
        tentativi_fatti += 1

        # Fornisce feedback all'utente in base al tentativo
        if guess < numero_da_indovinare:
            print("Troppo basso!")
        elif guess > numero_da_indovinare:
            print("Troppo alto!")
        else:
            print("Hai indovinato!")
            return

    # Se l'utente esaurisce i tentativi senza indovinare il numero, mostra il numero da indovinare
    print("Hai esaurito i tentativi. Il numero era:", numero_da_indovinare)

# Chiedi all'utente di specificare il range e il numero massimo di tentativi
inizio = int(input("Inserisci il numero di partenza del range: "))
fine = int(input("Inserisci il numero finale del range: "))
tentativi_massimi = int(input("Inserisci il numero massimo di tentativi: "))

# Esegui il gioco
gioco_indovina_numero(inizio, fine, tentativi_massimi)

#3. E-commerce Shopping Cart:
#Create a function that defines a product with a name, price, and quantity.
#Create a function that manages the shopping cart, allowing the user to add, remove, and view products in the cart.
#The function should calculate the cart total and apply any discounts or taxes.
#Implement a for loop to iterate over the items in the cart and print detailed information about each product and the total.
# Funzione per aggiungere un prodotto al carrello
def aggiungi_prodotto(carrello, nome, prezzo, quantita):
    carrello.append({"nome": nome, "prezzo": prezzo, "quantita": quantita})

# Funzione per rimuovere un prodotto dal carrello
def rimuovi_prodotto(carrello, nome):
    for prodotto in carrello:
        if prodotto["nome"] == nome:
            carrello.remove(prodotto)
            print(f"{nome} rimosso dal carrello.")
            return
    print("Prodotto non trovato nel carrello.")

# Funzione per visualizzare il carrello e calcolare il totale
def visualizza_carrello(carrello):
    print("\nCarrello:")
    totale = 0
    for prodotto in carrello:
        totale += prodotto["prezzo"] * prodotto["quantita"]
        print(f"Prodotto: {prodotto['nome']}, Prezzo: {prodotto['prezzo']}, Quantità: {prodotto['quantita']}")
    print(f"Totale: {totale}")

# Funzione principale per gestire il carrello
def gestisci_carrello():
    carrello = []  # Lista per memorizzare i prodotti nel carrello
    
    # Menu per l'utente
    while True:
        print("\n1. Aggiungi prodotto al carrello")
        print("2. Rimuovi prodotto dal carrello")
        print("3. Visualizza il carrello")
        print("4. Esci")
        
        scelta = input("Seleziona un'opzione: ")
        
        # Aggiungi prodotto al carrello
        if scelta == "1":
            nome_prodotto = input("Inserisci il nome del prodotto: ")
            prezzo_prodotto = float(input("Inserisci il prezzo del prodotto: "))
            quantita_prodotto = int(input("Inserisci la quantità del prodotto: "))
            aggiungi_prodotto(carrello, nome_prodotto, prezzo_prodotto, quantita_prodotto)
            print(f"{nome_prodotto} aggiunto al carrello.")
        
        # Rimuovi prodotto dal carrello
        elif scelta == "2":
            nome_prodotto = input("Inserisci il nome del prodotto da rimuovere: ")
            rimuovi_prodotto(carrello, nome_prodotto)
        
        # Visualizza il carrello
        elif scelta == "3":
            visualizza_carrello(carrello)
        
        # Esci
        elif scelta == "4":
            print("Grazie per aver utilizzato il carrello.")
            break
        
        else:
            print("Opzione non valida. Riprova.")

# Esegui la funzione per gestire il carrello
gestisci_carrello()

#4. Text Analysis:
#Create a function that reads a text file and counts the number of occurrences of each word.
#The function should print a report showing the most frequent words and their number of occurrences.
#You can use a for loop to iterate over the words in the text and a dictionary to store the occurrences.
#Implement error handling to handle missing files or other input issues.
def leggi_file(nome_file):
    # Apre il file in modalità lettura
    file = open(nome_file, 'r')
    # Legge il contenuto del file e lo restituisce come stringa
    contenuto = file.read()
    # Chiude il file
    file.close()
    return contenuto

# Funzione per l'analisi del testo
def analizza_testo(contenuto):
    # Divide la stringa in una lista di parole
    parole = contenuto.split()
    
    # Dizionario per memorizzare le occorrenze di ciascuna parola
    conteggio_parole = {}
    
    # Conta le occorrenze di ciascuna parola
    for parola in parole:
        # Rimuove eventuali caratteri di punteggiatura dalle parole
        parola = parola.strip('.,!?;:')
        
        # Converti la parola in minuscolo per evitare distinzioni tra maiuscole e minuscole
        parola = parola.lower()
        
        # Aggiorna il conteggio della parola nel dizionario
        conteggio_parole[parola] = conteggio_parole.get(parola, 0) + 1
    
    # Ordina il dizionario in base al numero di occorrenze delle parole
    conteggio_parole_ordinate = sorted(conteggio_parole.items(), key=lambda x: x[1], reverse=True)
    
    # Stampa il rapporto con le parole più frequenti e il loro conteggio
    print("Parole più frequenti nel testo:")
    for parola, conteggio in conteggio_parole_ordinate[:10]:  # Mostra le prime 10 parole più frequenti
        print(f"{parola}: {conteggio}")

# Nome del file da analizzare
nome_file = input("Inserisci il nome del file da analizzare: ")

# Legge il contenuto del file
contenuto_file = leggi_file(nome_file)

# Esegui la funzione di analisi del testo
analizza_testo(contenuto_file)


#5. Inventory Management System:
#Create a function that defines an item with a code, name, quantity, and price.
#Create a database or dictionary to store the items in inventory.
#Implement functions to add, remove, search, and update items in the inventory.
#Use for loops and conditional statements to manage the various inventory operations.
# Definizione della funzione per creare un nuovo elemento nell'inventario
def crea_elemento(codice, nome, quantita, prezzo):
    # Crea un dizionario che rappresenta l'elemento
    elemento = {"codice": codice, "nome": nome, "quantita": quantita, "prezzo": prezzo}
    return elemento

# Inizializzazione del database dell'inventario come un dizionario vuoto
inventario = {}

# Funzione per aggiungere un elemento all'inventario
def aggiungi_elemento(codice, nome, quantita, prezzo):
    # Crea un nuovo elemento
    nuovo_elemento = crea_elemento(codice, nome, quantita, prezzo)
    # Aggiunge il nuovo elemento al database dell'inventario
    inventario[codice] = nuovo_elemento
    print("Elemento aggiunto all'inventario.")

# Funzione per rimuovere un elemento dall'inventario
def rimuovi_elemento(codice):
    # Verifica se l'elemento esiste nell'inventario
    if codice in inventario:
        # Rimuove l'elemento dall'inventario
        del inventario[codice]
        print("Elemento rimosso dall'inventario.")
    else:
        print("Elemento non trovato nell'inventario.")

# Funzione per cercare un elemento nell'inventario
def cerca_elemento(codice):
    # Verifica se l'elemento esiste nell'inventario
    if codice in inventario:
        # Stampa le informazioni sull'elemento trovato
        print("Informazioni sull'elemento:")
        print("Codice:", inventario[codice]["codice"])
        print("Nome:", inventario[codice]["nome"])
        print("Quantità:", inventario[codice]["quantita"])
        print("Prezzo:", inventario[codice]["prezzo"])
    else:
        print("Elemento non trovato nell'inventario.")

# Funzione per aggiornare le informazioni di un elemento nell'inventario
def aggiorna_elemento(codice, nome, quantita, prezzo):
    # Verifica se l'elemento esiste nell'inventario
    if codice in inventario:
        # Aggiorna le informazioni dell'elemento
        inventario[codice]["nome"] = nome
        inventario[codice]["quantita"] = quantita
        inventario[codice]["prezzo"] = prezzo
        print("Informazioni dell'elemento aggiornate.")
    else:
        print("Elemento non trovato nell'inventario.")

# Esempi di utilizzo delle funzioni
aggiungi_elemento("001", "Prodotto A", 10, 20.0)
aggiungi_elemento("002", "Prodotto B", 15, 30.0)
cerca_elemento("001")
aggiorna_elemento("001", "Nuovo Prodotto A", 20, 25.0)
rimuovi_elemento("002")
cerca_elemento("002")
#6. Password Generator:
#Create a function that generates a random password with a specified length and desired character types (lowercase letters, uppercase letters, numbers, symbols).
#Allow the user to specify the password length and desired character types.
#Generate and return a random password that meets the user's criteria.
import random

def genera_password(lunghezza, lettere_minuscole, lettere_maiuscole, numeri, simboli):
    # Definiamo una stringa contenente tutti i possibili caratteri in base alle scelte dell'utente
    caratteri = ''
    if lettere_minuscole:
        caratteri += 'abcdefghijklmnopqrstuvwxyz'
    if lettere_maiuscole:
        caratteri += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if numeri:
        caratteri += '0123456789'
    if simboli:
        caratteri += '!@#$%^&*()_+=-[]{}|\\;:\'",.<>?'
    # Generiamo la password casuale scegliendo caratteri dalla stringa definita sopra
    password = ''.join(random.choice(caratteri) for _ in range(lunghezza))
    return password
# Esempio di utilizzo della funzione
lunghezza = 12  # Lunghezza desiderata della password
lettere_minuscole = True  # Includere lettere minuscole
lettere_maiuscole = True  # Includere lettere maiuscole
numeri = True  # Includere numeri
simboli = True  # Includere simboli

password_generata = genera_password(lunghezza, lettere_minuscole, lettere_maiuscole, numeri, simboli)
print("La password generata è:", password_generata)


#7. Roman Numeral Conversion:
#Create a function that converts a given integer to its Roman numeral representation.
#Handle numbers from 1 to 3999.
#Use a combination of string manipulation and conditional statements to build the Roman numeral.
def converti_in_numero_romano(numero):
    # Definiamo i simboli dei numeri romani e i corrispondenti valori
    simboli = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    valori = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    risultato = ''
    
    # Iteriamo attraverso i simboli e i valori per costruire il numero romano
    indice = 0
    while numero > 0:
        if numero >= valori[indice]:
            risultato += simboli[indice]
            numero -= valori[indice]
        else:
            indice += 1
    
    return risultato

# Esempio di utilizzo della funzione
numero_da_convertire = 354
numero_romano = converti_in_numero_romano(numero_da_convertire)
print("Il numero romano corrispondente a", numero_da_convertire, "è:", numero_romano)


#8. ATM Machine Simulator:

#Create a function that simulates an ATM machine.
#Initialize an account with a starting balance.
#Allow the user to perform transactions such as deposit, withdraw, and check balance.
#Validate transactions against the account balance and available funds.
#Provide appropriate feedback to the user for each transaction.
def crea_bancomat(saldo_iniziale):
    # Definiamo una funzione che crea un bancomat con un saldo iniziale specificato
    saldo = saldo_iniziale  # Inizializziamo il saldo del bancomat con il saldo iniziale fornito

    # Definiamo una funzione per depositare denaro nel bancomat
    def deposita(importo):
        nonlocal saldo  # Indichiamo che la variabile saldo non è locale, ma viene presa dallo scope della funzione madre
        if importo > 0:
            saldo += importo  # Aggiungiamo l'importo al saldo del bancomat
            return "Deposito effettuato con successo."
        else:
            return "Errore: l'importo del deposito deve essere maggiore di zero."

    # Definiamo una funzione per prelevare denaro dal bancomat
    def preleva(importo):
        nonlocal saldo  # Indichiamo che la variabile saldo non è locale, ma viene presa dallo scope della funzione madre
        if importo > 0:
            if importo <= saldo:  # Verifichiamo se ci sono fondi sufficienti nel bancomat per il prelievo
                saldo -= importo  # Sottraiamo l'importo dal saldo del bancomat
                return "Prelievo effettuato con successo."
            else:
                return "Errore: fondi insufficienti nel conto."
        else:
            return "Errore: l'importo del prelievo deve essere maggiore di zero."

    # Definiamo una funzione per controllare il saldo del bancomat
    def controlla_saldo():
        return f"Il saldo attuale è: {saldo}"

    return deposita, preleva, controlla_saldo  # Restituiamo le funzioni per depositare, prelevare e controllare il saldo del bancomat


# Creiamo un bancomat con un saldo iniziale di 1000
deposita, preleva, controlla_saldo = crea_bancomat(1000)

# Esempio di utilizzo delle funzioni del bancomat
print(deposita(500))  # Deposita 500
print(preleva(200))    # Preleva 200
print(controlla_saldo())  # Controlla il saldo attuale

#9. Caesar Cipher Encryption/Decryption
#Create functions for encrypting and decrypting a message using the Caesar cipher.
#Allow the user to specify the shift value (number of positions to shift each letter).
# Handle both encryption and decryption using the same function with appropriate adjustments.
#Encrypt and decrypt the given message using the specified shift value.
def cifra_cesare(messaggio, spostamento):
    cifrato = ""  # Inizializza la stringa cifrato
    for carattere in messaggio:
        # Cifra solo le lettere dell'alfabeto
        if carattere.isalpha():
            # Calcola il nuovo carattere cifrato e lo aggiunge alla stringa cifrato
            nuovo_carattere = chr((ord(carattere) - ord('a' if carattere.islower() else 'A') + spostamento) % 26 + ord('a' if carattere.islower() else 'A'))
            cifrato += nuovo_carattere
        else:
            # Aggiunge direttamente i caratteri non alfabetici alla stringa cifrato
            cifrato += carattere
    return cifrato

def decifra_cesare(cifrato, spostamento):
    # Decifra utilizzando uno spostamento negativo
    return cifra_cesare(cifrato, -spostamento)

# Funzione principale per eseguire la cifratura o decifratura
def main():
    messaggio = input("Inserisci il messaggio: ")
    scelta = input("Vuoi cifrare o decifrare? (cifra/decifra): ")
    spostamento = int(input("Inserisci lo spostamento: "))

    if scelta.lower() == "cifra":
        risultato = cifra_cesare(messaggio, spostamento)
        print("Il messaggio cifrato è:", risultato)
    elif scelta.lower() == "decifra":
        risultato = decifra_cesare(messaggio, spostamento)
        print("Il messaggio decifrato è:", risultato)
    else:
        print("Scelta non valida.")

# Eseguiamo il programma
main()

#10. Anagram Checker:
#Create a function that checks whether two given strings are anagrams of each other.
#Convert both strings to lowercase and remove any non-alphabetic characters.
#Sort the characters of each string and compare the sorted strings for equality.
#Indicate whether the strings are anagrams or not.
def sono_anagrammi(stringa1, stringa2):
    # Converto entrambe le stringhe in minuscolo
    stringa1 = stringa1.lower()
    stringa2 = stringa2.lower()

    # Rimuovo i caratteri non alfabetici dalle stringhe
    stringa1_pulita = ''
    for carattere in stringa1:
        if carattere.isalpha():
            stringa1_pulita += carattere

    stringa2_pulita = ''
    for carattere in stringa2:
        if carattere.isalpha():
            stringa2_pulita += carattere

    # Ordino i caratteri di ciascuna stringa
    stringa1_ordinata = ''.join(sorted(stringa1_pulita))
    stringa2_ordinata = ''.join(sorted(stringa2_pulita))

    # Confronto le stringhe ordinate per verificare se sono uguali
    if stringa1_ordinata == stringa2_ordinata:
        return "Le stringhe sono anagrammi l'una dell'altra."
    else:
        return "Le stringhe non sono anagrammi l'una dell'altra."

# Esempio di utilizzo della funzione
stringa1 = input("Inserisci la prima stringa: ")
stringa2 = input("Inserisci la seconda stringa: ")

risultato = sono_anagrammi(stringa1, stringa2)
print(risultato)

#11. Word Search Puzzle Solver:
#Create a function that solves a word search puzzle.
#Provide a 2D grid representing the puzzle and a list of words to find.
#Implement a backtracking algorithm to search for the words in the grid, marking visited cells to avoid repetition.
#Output the locations of the found words within the grid.
def risolvi_puzzle(puzzle, parole):
    # Funzione ausiliaria per controllare se una determinata parola può essere trovata a partire da una data posizione nel puzzle
    def trova_parola(puzzle, parola, riga, colonna, direzione):
        # Lunghezza della parola
        lunghezza_parola = len(parola)
        
        # Controlla se la parola può essere trovata partendo dalle coordinate date in una direzione specifica
        for i in range(lunghezza_parola):
            # Calcola le nuove coordinate basate sulla direzione
            nuova_riga = riga + direzione[0] * i
            nuova_colonna = colonna + direzione[1] * i
            
            # Verifica se le nuove coordinate sono all'interno del puzzle
            if nuova_riga < 0 or nuova_riga >= len(puzzle) or nuova_colonna < 0 or nuova_colonna >= len(puzzle[0]):
                return False  # Se la parola esce dai limiti del puzzle, non può essere trovata
            
            # Verifica se la lettera corrente corrisponde alla lettera della parola
            if puzzle[nuova_riga][nuova_colonna] != parola[i]:
                return False  # Se non corrisponde, la parola non può essere trovata
            
        return True  # Se tutte le lettere corrispondono, la parola è stata trovata

    # Funzione principale per risolvere il puzzle e trovare le parole
    risultati = {}  # Dizionario per memorizzare le posizioni delle parole trovate
    
    for parola in parole:
        for riga in range(len(puzzle)):
            for colonna in range(len(puzzle[0])):
                for direzione in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    if trova_parola(puzzle, parola, riga, colonna, direzione):
                        risultati[parola] = (riga, colonna)
    
    return risultati

# Esempio di utilizzo della funzione
puzzle = [
    ['A', 'B', 'C', 'D'],
    ['E', 'F', 'G', 'H'],
    ['I', 'J', 'K', 'L'],
    ['M', 'N', 'O', 'P']
]
parole_da_trovare = ['AB', 'FG', 'JKL', 'PN']
risultati = risolvi_puzzle(puzzle, parole_da_trovare)
print("Risultati:")
for parola, posizione in risultati.items():
    print(f"{parola}: {posizione}")

#12. Sieve of Eratosthenes Prime Number Generator:
#Create a function that generates a list of prime numbers up to a specified limit using the Sieve of Eratosthenes algorithm.
#Initialize an array of all numbers up to the limit, marking each number as prime initially.
#Iterate through the array, starting from 2, and mark every multiple of the current number as non-prime.
#The remaining unmarked numbers are the prime numbers within the limit.
#Return the list of prime numbers.
from math import sqrt

def genera_numeri_primi(limite):
    # Inizializza un array di tutti i numeri fino al limite, marcando ciascun numero come primo inizialmente
    numeri_primi = [True] * (limite + 1)
    numeri_primi[0] = numeri_primi[1] = False  # 0 e 1 non sono numeri primi

    # Itera attraverso l'array, partendo da 2, e marca ogni multiplo del numero corrente come non primo
    for numero in range(2, int(sqrt(limite)) + 1):
        if numeri_primi[numero]:
            for multiplo in range(numero * numero, limite + 1, numero):
                numeri_primi[multiplo] = False

    # I numeri non marcati sono i numeri primi all'interno del limite
    numeri_primi_generati = [numero for numero in range(limite + 1) if numeri_primi[numero]]
    return numeri_primi_generati

# Esempio di utilizzo della funzione per generare numeri primi fino a 50
limite = 50
primi_fino_a_limite = genera_numeri_primi(limite)
print("Numeri primi fino a", limite, ":", primi_fino_a_limite)

#13. Fractal Tree Generator:
#Create a function that generates a fractal tree using recursion.
#Specify the starting trunk length and branching angle.
#Draw the trunk and then recursively call the function to draw two branches at the specified angle, each with a shorter length.
#Repeat the branching process until a desired level of detail is reached.
def disegna_albero(lunghezza_tronco, angolo_ramificazione, livello_dettaglio):
    if livello_dettaglio == 0:
        return
    else:
        # Disegna il tronco
        print(' ' * livello_dettaglio + '*' * lunghezza_tronco)

        # Ramifica a sinistra
        disegna_albero(lunghezza_tronco * 0.8, angolo_ramificazione, livello_dettaglio - 1)

        # Ramifica a destra
        disegna_albero(lunghezza_tronco * 0.8, angolo_ramificazione, livello_dettaglio - 1)

# Chiamata alla funzione per disegnare l'albero
disegna_albero(10, 45, 5)

#14. Sudoku Solver:
#Create a function that solves a Sudoku puzzle using backtracking.
#Provide a 9x9 grid representing the puzzle with some numbers filled in and others left blank.
#Implement a backtracking algorithm to check for valid placements in empty cells, ensuring no row, column, or 3x3 subgrid contains duplicates.
#Solve the puzzle by filling in the remaining empty cells with valid numbers.
def risolvi_sudoku(griglia):
    # Trova la prossima cella vuota da riempire
    vuota = trova_vuota(griglia)
    
    # Se non ci sono più celle vuote, il sudoku è già risolto, quindi restituisci True
    if not vuota:
        return True
    
    # Estrai riga e colonna della cella vuota
    riga, colonna = vuota
    
    # Prova a riempire la cella vuota con un numero valido
    for numero in range(1, 10):
        if valido(griglia, numero, (riga, colonna)):
            griglia[riga][colonna] = numero  # Riempie la cella con il numero valido
            
            # Procede ricorsivamente alla risoluzione del sudoku
            if risolvi_sudoku(griglia):
                return True
            
            # Se la ricorsione non porta a una soluzione valida, reimposta la cella vuota
            griglia[riga][colonna] = 0
    
    # Se nessun numero valido può essere inserito nella cella, torna indietro e prova un'altra strada
    return False

def trova_vuota(griglia):
    # Trova la prossima cella vuota nella griglia
    for riga in range(9):
        for colonna in range(9):
            if griglia[riga][colonna] == 0:
                return (riga, colonna)  # Restituisce la posizione della cella vuota
    return None  # Se non ci sono più celle vuote, restituisce None

def valido(griglia, numero, posizione):
    # Controlla se il numero può essere inserito nella posizione specificata senza violare le regole del sudoku
    
    # Controllo sulla riga
    for i in range(9):
        if griglia[posizione[0]][i] == numero and i != posizione[1]:
            return False
    
    # Controllo sulla colonna
    for i in range(9):
        if griglia[i][posizione[1]] == numero and i != posizione[0]:
            return False
    
    # Controllo sulla sottogriglia 3x3
    box_riga = posizione[0] // 3
    box_colonna = posizione[1] // 3
    
    for i in range(box_riga * 3, box_riga * 3 + 3):
        for j in range(box_colonna * 3, box_colonna * 3 + 3):
            if griglia[i][j] == numero and (i, j) != posizione:
                return False
    
    # Se il numero non viola nessuna regola, è valido
    return True

# Griglia di esempio
griglia_sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Risolvi il Sudoku
risolvi_sudoku(griglia_sudoku)

# Stampa la griglia risolta
for riga in griglia_sudoku:
    print(riga)


#15. Text Editor with Basic Functionality:
#Create a simple text editor that allows the user to open, edit, and save text files.
#Implement basic functionality such as inserting, deleting, and copying text.
#Provide undo/redo functionality to allow users to reverse actions.
#Save the edited text to a file when the user chooses to save.
# Definizione della funzione principale
def main():
    # Inizializza una stringa vuota per contenere il testo
    testo = ""

    # Menu principale
    while True:
        print("Scegli un'opzione:")
        print("1. Apri un file")
        print("2. Modifica il testo")
        print("3. Salva il testo")
        print("4. Esci")
        scelta = input("Scelta: ")

        # Opzione 1: Apri un file
        if scelta == "1":
            nome_file = input("Inserisci il nome del file: ")
            testo = apri_file(nome_file)

        # Opzione 2: Modifica il testo
        elif scelta == "2":
            print("Cosa vuoi fare?")
            print("a. Inserisci del testo")
            print("b. Cancella del testo")
            print("c. Copia del testo")
            azione = input("Scelta: ")

            if azione == "a":
                testo = inserisci_testo(testo)
            elif azione == "b":
                testo = cancella_testo(testo)
            elif azione == "c":
                testo = copia_testo(testo)

        # Opzione 3: Salva il testo
        elif scelta == "3":
            nome_file = input("Inserisci il nome del file per salvare: ")
            salva_file(testo, nome_file)

        # Opzione 4: Esci dal programma
        elif scelta == "4":
            print("Grazie per aver usato il nostro editor di testo!")
            break
        else:
            print("Scelta non valida. Riprova.")

# Funzione per aprire un file
def apri_file(nome_file):
    try:
        with open(nome_file, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("Il file specificato non esiste.")
        return ""

# Funzione per inserire del testo
def inserisci_testo(testo):
    nuovo_testo = input("Inserisci del testo: ")
    return testo + nuovo_testo

# Funzione per cancellare del testo
def cancella_testo(testo):
    posizione = int(input("Inserisci la posizione da cui cancellare: "))
    lunghezza = int(input("Inserisci la lunghezza del testo da cancellare: "))
    return testo[:posizione] + testo[posizione + lunghezza:]

# Funzione per copiare del testo
def copia_testo(testo):
    posizione_inizio = int(input("Inserisci la posizione di inizio della copia: "))
    posizione_fine = int(input("Inserisci la posizione di fine della copia: "))
    return testo[posizione_inizio:posizione_fine]

# Funzione per salvare il testo su file
def salva_file(testo, nome_file):
    with open(nome_file, "w") as file:
        file.write(testo)
    print("Il testo è stato salvato con successo nel file", nome_file)

# Avvio del programma
if __name__ == "__main__":
    main()
