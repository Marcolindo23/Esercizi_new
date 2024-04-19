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

    






