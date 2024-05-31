class Film:
    def __init__(self, Titolo: str, Durata: int):
        self.Titolo = Titolo
        self.Durata = Durata

class Sala:
    def __init__(self, Numero_Sala: int, film: Film, Numero_Posti_Sala: int):
        self.Numero_Sala = Numero_Sala
        self.film = film
        self.Numero_Posti_Sala = Numero_Posti_Sala
        self.Numero_Posti_Prenotati = 0
    
    def prenota_posti(self, num_posti: int):
        if self.posti_disponibili() >= num_posti:
            self.Numero_Posti_Prenotati += num_posti
            return f"{num_posti} posti prenotati per il film '{self.film.Titolo}' in Sala {self.Numero_Sala}."
        else:
            return "Errore: non ci sono abbastanza posti disponibili."
    
    def posti_disponibili(self):
        return self.Numero_Posti_Sala - self.Numero_Posti_Prenotati

class Cinema:
    def __init__(self):
        self.sale : list[Sala] = []

    def aggiungi_sala(self, sala: Sala):
        self.sale.append(sala)

    def prenota_film(self, Titolo_Film: str, num_posti: int):
        for sala in self.sale:
            if sala.film.Titolo == Titolo_Film:
                risultato = sala.prenota_posti(num_posti)
                print(risultato)
                return
        print(f"Errore: film '{Titolo_Film}' non trovato.")


	
##############################################################################################################################################################
class Prodotto:
    def __init__(self, nome: str, quantità: int):
        self.nome = nome
        self.quantità = quantità

class Magazzino:
    def __init__(self):
        self.prodotti: list[Prodotto] = []   
    
    def aggiungi_prodotto(self, prodotto: Prodotto):
        for p in self.prodotti:
            if p.nome == prodotto.nome:
                p.quantità += p.quantità
                return self.prodotti.append(prodotto)

    def cerca_prodotto(self, nome: str):
        for p in self.prodotti:
            if p.nome == nome:
                return p

    def verifica_disponibilità(self, nome: str) -> str:
        prodotto = self.cerca_prodotto(nome)
        if prodotto and prodotto.quantità > 0:
            return f"Il prodotto {nome} è disponibile con {prodotto.quantità} unità."
        else:
            return f"Il prodotto {nome} non è disponibile."

    def mostra_tutti_i_prodotti(self):
        if not self.prodotti:
            print("Il magazzino è vuoto.")
        for prodotto in self.prodotti:
            print(f"Prodotto: {prodotto.nome}, Quantità: {prodotto.quantità}")

