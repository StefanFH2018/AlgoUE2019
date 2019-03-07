#!/usr/bin/env python

def fibef_n(nte_Fibzahl):
    a = 0
    b = 1

    for i in range(nte_Fibzahl):

        a, b = b, a + b

    return a



def fibef_alle(nte_Fibzahl):
    a = 0
    b = 1
    temp = [0]

    for i in range(nte_Fibzahl):

        a, b = b, a + b
        temp.append(a)

    return temp

eingabe_zahl = int(input("Geben Sie an bis zu welcher Fibonaci-Zahl berechnet werden soll: "))
eingabe_entscheidung = input("Wollen Sie alle Fibonaci-Zahlen bis zur n-ten  anzeigen? (y=1/n=0)")

import time
start = time.time()

if eingabe_entscheidung == 1:
    print(fibef_alle(eingabe_zahl))
if eingabe_entscheidung == 0:
    print(fibef_n(eingabe_zahl))

end = time.time()
print("Laufzeit[s]: ")
print(end - start)