#Scrivi una funzione che, dato un numero intero, determina se è un "numero magico". Un numero magico è definito come un numero che contiene il numero 7.
def is_magic_number(num: int) -> bool:
    num_str=str(num)
    if "7" in num_str:
        return True
    else:
        return False


#Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. 
#Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.
def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    nuova_lista = lista[:]
    
    # Itero attraverso le chiavi e i valori del dizionario
    for elemento, quantità in da_rimuovere.items():
        # Controllo se l'elemento è presente nella lista
        if elemento in nuova_lista:
            # Rimuovo l'elemento dalla lista il numero di volte specificato
            for _ in range(quantità):
                nuova_lista.remove(elemento)
    
    return nuova_lista


#Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario.
def aggrega_voti(voti: dict) -> dict[str:list[int]]:
    risultato = {}
    
    # Itero attraverso ogni dizionario nella lista dei voti
    for voto in voti:
        nome_studente = voto['nome']
        voto_studente = voto['voto']
        
        # Se lo studente è già presente nel dizionario dei risultati, aggiungo il voto alla lista dei suoi voti
        if nome_studente in risultato:
            risultato[nome_studente].append(voto_studente)
        # Altrimenti, creo una nuova chiave per lo studente e inizializzo la lista dei suoi voti con il primo voto
        else:
            risultato[nome_studente] = [voto_studente]
    
    return risultato


#Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, 
#scontati del 10%.
def filtra_e_mappa(prodotti: dict[str:float]) -> list[str:float]:
    dizionario_prodotti_scontati = {}
    prezzo_scontato = (value*10)/100
    for product, value in prodotti.items():
        if prezzo_scontato > 20:
            dizionario_prodotti_scontati[product] = prezzo_scontato
    return dizionario_prodotti_scontati
        

        