stringa: str="Ciao come stai. Tutto bene. Ciao io sto bene"
#funzione che prende in input un dizionario (e.s. d={"Ciao":2, "Hello":3}) restituendo un nuovo dizionario fatto così:
#d1={"Ciao":2/5, "Hello":3/5} dove 5 è la somma dei valori di d, ossia 2+3=5
d={"Ciao":2, "Hello":3}
def rewrite_dict(d: dict[str, int]):
    print(f"Il dizionario di input é {d}")
    somma=sum(list(d.values()))
    out={}
    for key in d:
        out[key]=d[key]/somma
    return out
output=rewrite_dict(d)
print(f"Il nuovo output è {output}")

def sottrazione(x:float, y:float):
    sottrazione: float=x-y
    return sottrazione
x=float(input("Il primo numero è:"))
y=float(input("Il secondo numero è:"))
print(f"La sottrazione dei due numeri è: {sottrazione(x,y)}")

#Funzione che prende in input una lista di valori reali e restituisce la mediana di questa lista
def median(l: list[float]):
    l.sort()
    if len(l) % 2 == 1:
        mid = len(l) // 2 
        mediana = l[mid]
        return mediana
    else:
        mid = len(l) // 2
        mid1 = mid -1 
        mediana = (l[mid] + l[mid1]) / 2
        return mediana

s_input: str = input("Inserisci dei numeri delimitati da spazi: ")
l: list[str] = s_input.split()
l1: list[float] = []
for elem in l:
    l1.append(float(elem))
print(l)
print(l1)
mediana=median(l1)
print(f"La mediana della lista è: {mediana}")


def diff_com(l3: list[float]):
    sottrazione1=0
    for i in range(1, len(l3)):
        sottrazione1-=l3[i]
    return sottrazione1
s_input: str = input("Inserisci dei numeri delimitati da spazi: ")
l3: list[str] = s_input.split()
l4: list[float] = []
for elem in l3:
    l4.append(float(elem))
print(l3)
print(l4)
sottrazione1=diff_com(l4)
print(f"La differenza comulativa é: {sottrazione1}")

def subtract_all(x: list[float], y: float) -> list[float]:
    res: list[float]=[]
    for elem in x:
        c: float=elem-y
        res.append(c)
    return res
mylist: list[float]=[1,2,3,4,5]
y: float=10
result=subtract_all(mylist,y)
print(f"La nuova lista è {result}")


def subtract_all(mylist1: list[float], z: float) -> list[float]:
    risultato: list[float]=[]
    for i in range(len(mylist1)):
        t=mylist1[i]-z[i]
        risultato.append(t)
    return risultato
mylist1: list[float]=[1,2,3,4,5]
z: list[float]=[2,3,4,5,6]
risultato=subtract_all(mylist1,z)
print(f"La lista nuova è: {risultato}")


s: str = "La meccanica quantistica è la teoria fisica che descrive il comportamento della materia, della radiazione e le reciproche interazioni, con particolare riguardo ai fenomeni caratteristici della scala di lunghezza o di energia atomica e subatomica, dove le precedenti teorie classiche risultano inadeguate. Come caratteristica fondamentale, la meccanica quantistica descrive la radiazione e la materia sia come fenomeni ondulatori che come entità particellari, al contrario della meccanica classica, che descrive la luce solamente come un'onda e, ad esempio, l'elettrone solo come una particella. Questa inaspettata e controintuitiva proprietà della realtà fisica, chiamata dualismo onda-particella, è la principale ragione del fallimento delle teorie sviluppate fino al XIX secolo nella descrizione degli atomi e delle molecole. La relazione tra natura ondulatoria e corpuscolare è enunciata nel principio di complementarità e formalizzata nel principio di indeterminazione di Heisenberg. Esistono numerosi formalismi matematici equivalenti della teoria, come la meccanica ondulatoria e la meccanica delle matrici; al contrario, ne esistono numerose e discordanti interpretazioni riguardo all'essenza ultima del cosmo e della natura, che hanno dato vita a un dibattito tuttora aperto nell'ambito della filosofia della scienza. La meccanica quantistica rappresenta, assieme alla teoria della relatività, uno spartiacque rispetto alla fisica classica, portando alla nascita della fisica moderna. Attraverso la teoria quantistica dei campi, generalizzazione della formulazione originale che include il principio di relatività ristretta, essa è a fondamento di molte altre branche della fisica, come la fisica atomica, la fisica della materia condensata, la fisica nucleare, la fisica delle particelle, la chimica quantistica."

def counter(s: str) -> list[int]:

#Questa funzione prende una stringa in input e restituisce una lista costruita nel modo seguente:
#Il primo elemento della lista contiene il numero di caratteri nella stringa
#Il secondo elemento della lista contiene il numero di parole nella stringa
#Il terzo elemento della lista contiene il numero di parole distinte nella stringa
#Il quarto elemnto della lista contiene il numero di frasi nella lista

    risultato=[]
    lunghezza_stringa=len(s)
    numero_caratteri=len(s.replace("",""))
    risultato.append(numero_caratteri)
    print(risultato)
    numero_parole=len(s.split())
    risultato.append(numero_parole)
    print(risultato)
    Parole=s.split()
    Parole_Distinte=set(Parole)
    risultato.append(Parole_Distinte)
    print(risultato)
    numero_frasi=len(s.split("."))
    risultato.append(numero_frasi)
    print(risultato)
    return risultato
risultato=counter(s)
print(f"La lista con le informazione della stringa è: {risultato}")

#Questa funzione conta il numero di occorrenza delle parole di una stringa
#e.s. se la stringa é: "ciao come stai. tutto bene. ciao io sto bene"
#il risultato deve essere un dizionario
def word_count(s: str) -> dict[str, int]:
    lunghezza_stringa1=len(stringa)
    q=stringa.replace(".","").replace(";","").replace(",","").replace("?","").replace("!","").replace(":","")
    parole2: list[str]=stringa.split()
    d: dict[str, int]=dict()
    for parola1 in parole2:
        if parola1 not in d:
            d[parola1]=1
        else:
            d[parola1]+=1
    d_filtered: dict[str, int]=dict()
    d: dict[str, int]=dict()
    for key, val in d.items():
        if val >1:
            d_filtered[key]=key
        return d_filtered
    
d=word_count(stringa)
d_filtered=word_count(stringa)
print(f"Il dizionario nuovo è: {d}")
print(f"Il dizionario filtrato é: {d_filtered}")

def is_palindrome(f: str) ->bool:
    
    s: str=stringa.lower().replace(" ","")
    i: int=0
    while i<len(s):
        j=len(s)-(i+1)
        if s[i]!=s[j]:
            return False
        else:
            i+=1
            return True

print(is_palindrome(s))



   






