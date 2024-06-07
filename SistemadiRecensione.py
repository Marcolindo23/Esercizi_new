class Media:
    def __init__(self, title: str, reviews: list[int]):
        self.title = title
        self.reviews = reviews
    
    def set_title(self, title):
        self.title = title
    
    def get_title(self):
        return self.title

    def aggiungiValutazione(self, voto):
        if 1<= voto <= 5:
            self.reviews.append(voto)
    def getMedia(self):
        if len(self.reviews) == 0:
            return 0
        else: 
            return sum(self.reviews)/len(self.reviews)
    def getRate(self):
        media = self.getMedia()
        if media == 0:
            return "Nessuna Valutazione"
        elif media < 1.5:
            return "Terribile"
        elif media < 2.5:
            return "Brutto"
        elif media < 3.5:
            return "Normale"
        elif media < 4.5:
            return "Bello"
        else:
            return "Grandioso"
    def ratePercentage(self, voto):
        if len(self.reviews) == 0:
            return 0
        else:
            return (self.reviews.count(voto)/len(self.reviews))*100
    
    def recensione(self):
        print(f"Titolo: {self.get_title()}")
        print(f"Media Delle Valutazioni: {self.getMedia():.2f}")
        print(f"Giudizio: {self.getRate()}")
        for i in range(1,6):
            print(f"Percentuale di Valutazione {i}: {self.ratePercentage(i):.2f}")
class Film(Media):
    def __init__(self, title, director, duration):
        super().__init__(title)
        self.director = director
        self.duration = duration
    
    def set_director(self, director):
        self.director = director
    
    def get_director(self):
        return self.director

    def set_duration(self, duration):
        self.duration = duration

    def get_duration(self):
        return self.duration

    def recensione(self):
        super().recensione()
        print(f"Regista: {self.get_director()}")
        print(f"Durata del Film: {self.get_duration()} minuti")




film1 = Film("The Shawshank Redemption", "Frank Darabont", 142)
recensioni_film1 = [5, 4, 4, 3, 5, 2, 4, 3, 4, 5]
for voto in recensioni_film1:
    film1.aggiungiValutazione(voto)
print(f"Recensioni del primo film:")
film1.recensione()

film2 = Film("Oppenheimer", "Christopher Nolan", 180)
recensioni_film2 = [3, 3, 4, 2, 1, 3, 2, 4, 3, 3]
for voto in recensioni_film2:
    film2.aggiungiValutazione(voto)
print(f"\nRecensioni del secondo film:")
film2.recensione()

media = Media("1984")
recensioni_media = [5, 3, 4, 4, 2, 3, 5, 4, 2, 1]
for voto in recensioni_media:
    media.aggiungiValutazione(voto)
print(f"\nRecensioni del Media:")
media.recensione()











              

    
            


