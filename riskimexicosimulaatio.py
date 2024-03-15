import random
from collections import Counter
import matplotlib.pyplot as plt
import time

#Heittää noppaa ja antaa tuloksen. Tulos säilötään kokonaislukuna sekä uusien heittojen määränä.
def heita():
    tulos = [0,0]
    noppa1 = random.randint(1, 6)
    noppa2 = random.randint(1, 6)
    
    if noppa1 > noppa2:
        tulos[0] = noppa1 * 10 + noppa2
        tulos[1] = 0
    if noppa2 > noppa1:
        tulos[0] = noppa2 * 10 + noppa1
        tulos[1] = 0
    if noppa1 == noppa2:
        tulos[0] = noppa1 * 10 + noppa2
        tulos[1] = noppa1
    return tulos


#lisää listaan arvon ja poistaa vanhimman
def lisaaListaan(lista, tulos):
    lista.insert(0,tulos)
    lista.pop()


#Pelaa yhden kierroksen peliä
def pelaa():
    tulokset3 = [0,0,0]
    heittojaJaljella = 0
    mexicot = 0
    tulos = [0,0]

    #Tässä suoritetaan aloitusheitto. Aloitusta pelataan kunnes saadaan pari tai 21.
    while tulos[1] < 1 and tulos[0] != 21:
        tulos = heita()
        lisaaListaan(tulokset3, tulos)
        if all(element == tulokset3[0] for element in tulokset3):
            mexicot += 1
        heittojaJaljella = tulos[1] 
        if tulos[0] == 21:
            mexicot += 1


    #Pelataan loput heitot pois. Lisätään mexiot tuloksiin.
    while heittojaJaljella > 0: 
        tulos = heita()
        lisaaListaan(tulokset3, tulos)
        if all(element == tulokset3[0] for element in tulokset3):
            mexicot += 1
        if tulos[0] == 21:
            mexicot += 1
        if tulos[1] > 0:
            heittojaJaljella += tulos[1] 
        heittojaJaljella -= 1
    
    return mexicot


def piirra(tulokset):
    x_positions = range(0, len(tulokset) )
    plt.bar(x_positions, tulokset, color='blue')
    #plt.yscale('log') 
    plt.xlabel('mexicojen määrä')
    plt.ylabel('%')
    plt.title('Mexicojen määrä kaikissa peleissä')
    plt.show()
    

#Lasketaan suoritusnopeus
def lopetusaika():
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")

#Tulostetaan halutut tiedot
def printtaa(iteraatiot, tulokset):
    print("=============")
    print(f"iteraatiot: {iteraatiot}")
    print("=============")
    print(counts)
    print("=============\nTulokset")
    for i in range(len(tulokset)):
        print(f"{i}: {round(tulokset[i], 5)} %")
    print("=============")


'''
Pääohjelma. Iteraatioihin syötetään haluttujen suoritusten määrä ja ohjelma
pelaa peliä sekä tulostaa tulokset eli mexicojen saamisen todennäköisyyden
'''
if __name__ == "__main__":
    start_time = time.time()
    mexicotperpeli = []
    iteraatiot = 100000

    #Pelataan peliä ja laitetaan tulos listaan
    for i in range(iteraatiot):
        mexicotperpeli.append(pelaa())
    
    counts = Counter(mexicotperpeli)
    tulokset = []
    for i in range(max(mexicotperpeli) + 1):
        tulokset.append(counts[i]/iteraatiot*100)

    printtaa(iteraatiot, tulokset)

    lopetusaika()
    piirra(tulokset)