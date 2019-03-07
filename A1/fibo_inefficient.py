#!/usr/bin/env python

def fibin_n(nte_Fibzahl):
    if nte_Fibzahl == 0:
        return 0
    elif nte_Fibzahl == 1:
        return 1
    else:
        return fibin_n(nte_Fibzahl - 1) + fibin_n(nte_Fibzahl - 2)



def fibin_alle(nte_Fibzahl):
    def fibin_n(nte_Fibzahl):
        if nte_Fibzahl == 0:
            return 0
        elif nte_Fibzahl == 1:
            return 1
        else:
            return fibin_n(nte_Fibzahl - 1) + fibin_n(nte_Fibzahl - 2)

    temp = []
    for i in range(eingabe_zahl+1):
        a = fibin_n(i)
        temp.append(a)
    print(temp)

eingabe_zahl = int(input("Geben Sie an bis zu welcher Fibonaci-Zahl berechnet werden soll: "))
eingabe_entscheidung = int(input("Wollen Sie alle Fibonaci-Zahlen bis zur n-ten  anzeigen? (y=1/n=0): "))

import time
start = time.time()

if eingabe_entscheidung == 0:
    print(fibin_n(eingabe_zahl))
if eingabe_entscheidung == 1:
    print(fibin_alle(eingabe_zahl))

end = time.time()
print("Laufzeit[s]: ")
print(end - start)
