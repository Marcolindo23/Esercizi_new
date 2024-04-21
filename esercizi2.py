name="Ambrogio"
print("Ciao", name, "come stai?")
print(name.upper())
print(name.lower())
print(name.title())
name1="Albert Einstein"
print(name1, "diceva:", '"A person who never made a mistake never tried anything new"')
names=["Edoardo", "Flavio"]
print(names[0])
print(names[-1])
print("Ciao", names[0], "come stai?")
print("Ciao", names[-1], "come stai?")
Trasporto=["Ferrari", "Autobus"]
print("Il mio sogno sarebbe guidare una", Trasporto[0], "un giorno")
print("Per venire a lezione uso l'", Trasporto[-1])
numbers=[]
lunghezza=int(input("La lunghezza della lista è:"))
for i in range(1, lunghezza+1):
    numbers.append(i)
print("Lista Numbers:", numbers)
seconds=10
while seconds>0:
    print(seconds)
    seconds-=1
print("Time's up!")
d={'pippo':2, 'pluto':1, 'topolino':5}
keys=list(d.keys())
i=0
somma=0
while i<len(keys):
    key=keys[i]
    print(f'key={key} --> {d[key]}')
    val=d[key]
    somma+=val
    i+=1
    print(somma)
print(somma)
somma=sum(list(d.values()))
d1={}
for key in d:
    d1[key]=d[key]/somma
print(d)
print(d1)
import random
for _ in range[10]:
    numeri=[random.randint[1,100]]
print("lista numeri:",numeri)
d={}
somma_pari=0
somma_dispari=0
for i in numeri:
    if i%2==0:
        somma_pari+=i
    else:
        somma_dispari+=i
d['somma pari']=somma_pari
d['somma dispari']=somma_dispari
print('dizionario delle somme:', d)
        

 

