import random
def visualizza_posizione(posizione_Tartaruga, posizione_Lepre):
    percorso = ['-'] * 70
    if posizione_Tartaruga == posizione_Lepre:
        percorso[posizione_Tartaruga-1] = 'OUCH!!!'
    else:
        if posizione_Tartaruga > 0 and posizione_Tartaruga <= 70:
            percorso[posizione_Tartaruga - 1] = 'T'
        if posizione_Lepre > 0 and posizione_Lepre <= 70:
            percorso[posizione_Lepre - 1] = 'H'
    return "".join(percorso)

def muovi_Tartaruga(posizione):
    mossa = random.randint(1, 10)
    if mossa <= 5:
        posizione +=3
    elif mossa <= 7:
        posizione -= 6
    else:
        posizione += 1
    return max(1, min(70, posizione))

def muovi_Lepre(posizione):
    mossa = random.randint(1, 10)
    if mossa <= 2:
        pass
    elif mossa <= 4:
        posizione += 9
    elif mossa == 5:
        posizione -= 12
    elif mossa <= 8:
        posizione += 1
    else:
        posizione -= 2
    return max(1, min(70, posizione))

def gara():
    print("BANG !!!!! AND THEY'RE OFF !!!!!")
    
    pos_Tartaruga = 1
    pos_Lepre = 1

    while pos_Tartaruga < 70 and pos_Lepre < 70:
        print(visualizza_posizione(pos_Tartaruga, pos_Lepre))
        pos_Tartaruga = muovi_Tartaruga(pos_Tartaruga)
        pos_Lepre = muovi_Lepre(pos_Lepre)
        if pos_Tartaruga >= 70 and pos_Lepre >= 70:
            print("IT'S A TIE")
        elif pos_Tartaruga >= 70:
            print( "TORTOISE WINS! || VAY!!!")
        elif pos_Lepre >= 70:
            print("HARE WINS || YUCH!!!")
            
gara()
    




