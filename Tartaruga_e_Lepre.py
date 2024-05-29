import random

def visualizza_posizione(posizione_Tartaruga: int, posizione_Lepre: int):
    percorso = ['-'] * 70
    if posizione_Tartaruga == posizione_Lepre:
        percorso[posizione_Tartaruga-1] = 'OUCH!!!'
    else:
        if posizione_Tartaruga > 0 and posizione_Tartaruga <= 70:
            percorso[posizione_Tartaruga - 1] = 'T'
        if posizione_Lepre > 0 and posizione_Lepre <= 70:
            percorso[posizione_Lepre - 1] = 'H'
    print("".join(percorso))

def muovi_Tartaruga(posizione: int, meteo: str):
    mossa = random.randint(1, 10)
    penalita = 1 if meteo == "Pioggia" else 0

    if mossa <= 5:
        posizione += 3 - penalita
    elif mossa <= 7:
        posizione -= 6 - penalita
    else:
        posizione += 1 - penalita

    return max(1, min(70, posizione))

def muovi_Lepre(posizione: int, meteo: str):
    mossa = random.randint(1, 10)
    penalita = 2 if meteo == "Pioggia" else 0

    if mossa <= 2:
        pass
    elif mossa <= 4:
        posizione += 9 - penalita
    elif mossa == 5:
        posizione -= 12 - penalita
    elif mossa <= 8:
        posizione += 1 - penalita
    else:
        posizione -= 2 - penalita

    return max(1, min(70, posizione))

def cambia_meteo(tick: int):
    if (tick // 10) % 2 == 0:
        return 'Pioggia'
    else:
        return 'Soleggiato'

def gara():
    print("BANG !!!!! AND THEY'RE OFF !!!!!")
    
    pos_Tartaruga = 1
    pos_Lepre = 1
    tick = 0

    while pos_Tartaruga < 70 and pos_Lepre < 70:
        meteo = cambia_meteo(tick)
        print(f"Tick: {tick+1} Meteo: {meteo}")
        pos_Tartaruga = muovi_Tartaruga(pos_Tartaruga, meteo)
        pos_Lepre = muovi_Lepre(pos_Lepre, meteo)
        visualizza_posizione(pos_Tartaruga, pos_Lepre)
        if pos_Tartaruga >= 70 and pos_Lepre >= 70:
            print("IT'S A TIE")
            break
        elif pos_Tartaruga >= 70:
            print("TORTOISE WINS! || VAY!!!")
            break
        elif pos_Lepre >= 70:
            print("HARE WINS || YUCH!!!")
            break
        
        tick += 1

gara()






