#!/usr/bin/python3

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

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-n', '--numbers',type = int, help = 'geben Sie die gewünschte Fibonaci-Zahl an')
parser.add_argument('-a','--all', action = 'store_true', default= False, help = 'falls gewünscht können alle Fibonaci-Zahlen bis n ausgegeben werden')
#parser.add_argument('-h','--help', help ='zuerst ist die gewünschte Fibonaci-Zahl anzugeben und danach anzugeben ob alle oder nur die letzte Zahl ausgegeben werden soll')

args = parser.parse_args()


eingabe_zahl = int(args.numbers) #int(input("Geben Sie an bis zu welcher Fibonaci-Zahl berechnet werden soll: "))
eingabe_entscheidung = (args.all)#int(input("Wollen Sie alle Fibonaci-Zahlen bis zur n-ten  anzeigen? (y=1/n=0): "))


import time
start = time.time()

#if eingabe_entscheidung == 0:

if args.all:
#if eingabe_entscheidung == 1:
    print(fibin_alle(eingabe_zahl))
else:
    print(fibin_n(eingabe_zahl))

end = time.time()
print("Laufzeit[s]: ")
print(end - start)
