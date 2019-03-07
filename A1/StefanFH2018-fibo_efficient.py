#!/usr/bin/python3

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


from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-n', '--numbers',type = int, help = 'geben Sie die gewünschte Fibonaci-Zahl an')
parser.add_argument('-a','--all', action = 'store_true', default= False, help = 'falls gewünscht können alle Fibonaci-Zahlen bis n ausgegeben werden')

args = parser.parse_args()

eingabe_zahl = int(args.numbers)#int(input("Geben Sie an bis zu welcher Fibonaci-Zahl berechnet werden soll: "))
eingabe_entscheidung = (args.all)#input("Wollen Sie alle Fibonaci-Zahlen bis zur n-ten  anzeigen? (y=1/n=0)")

import time
start = time.time()

#if eingabe_entscheidung == 1:
if args.all:
    print(fibef_alle(eingabe_zahl))

#if eingabe_entscheidung == 0:
else:
    print(fibef_n(eingabe_zahl))

end = time.time()
print("Laufzeit[s]: ")
print(end - start)