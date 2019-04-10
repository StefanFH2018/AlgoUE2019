#!/usr/bin/python3

from Bio import SeqIO
from Bio.Seq import Seq
from argparse import ArgumentParser
from Bio.Alphabet import generic_dna
import sys

eingabe = ArgumentParser()
eingabe.add_argument('-ma', '--match', default=1, help="Wert für Übereinstimmung der Nukleotide (Default-Wert = -1)")
eingabe.add_argument('-mi', '--missmatch', default=-1, help="Wert für keine Übereinstimmung der Nukleotide (Default-Wert = -1)")
eingabe.add_argument('-g', '--gap', default=-2, help="Wert für eine Lücke im Alignement (Default-Wert = -2)")

file_input = SeqIO.parse(sys.stdin, "fasta")

i = 0
for sequence in file_input:
    if i == 0:
        sequence1 = sequence.seq
        ID1 = sequence.id
    elif i == 1:
        sequence2 = sequence.seq
        ID2 = sequence.id
    i+=1

scor_wert = [[0]]
pfad = [[" "]]

line_erz = len(sequence1) + 1
column_erz = len(sequence2) + 1

for i in range(1, column_erz, 1):
    scor_wert[0].append(scor_wert[0][i - 1] + eingabe.parse_args().gap)
    pfad[0].append("rechts")

iterator1 = 0
iterator2 = 0

for line in range(1, line_erz, 1):
    scor_wert.append([scor_wert[line - 1][0] + eingabe.parse_args().gap])
    pfad.append(["unten"])
    for column in range(1, column_erz, 1):
        vertical = scor_wert[line - 1][column] + eingabe.parse_args().gap
        horizontal = scor_wert[line][column - 1] + eingabe.parse_args().gap
        if (sequence1[iterator1] == sequence2[iterator2]):
            diagonal = scor_wert[line - 1][column - 1] + eingabe.parse_args().match
        else:
            diagonal = scor_wert[line - 1][column - 1] + eingabe.parse_args().missmatch

        if horizontal >= vertical and horizontal > diagonal:
            scor_wert[line].append(horizontal)
            pfad[line].append("rechts")
        elif vertical > horizontal and vertical > diagonal:
            scor_wert[line].append(vertical)
            pfad[line].append("unten")
        elif diagonal >= horizontal and diagonal >= vertical:
            scor_wert[line].append(diagonal)
            pfad[line].append("d")
        iterator2 += 1
    iterator1 +=1
    iterator2 = 0

column = len(pfad[0]) - 1
line = len(pfad) - 1
pfad_zurueck = ""

while(line > 0 or column > 0):
    if pfad[line][column] == "d":
        pfad_zurueck += "d"
        line -= 1
        column -= 1
    elif pfad[line][column] == "unten":
        pfad_zurueck += "unten"
        line -= 1
    elif pfad[line][column] == "rechts":
        pfad_zurueck += "rechts"
        column -= 1
    elif pfad[line][column] == " ":
        break
    else:
        print("Wrong element in path matrix.")
pfad_zurueck = pfad_zurueck[::-1]

alignment = ["","",""]
iterator1 = 0
iterator2 = 0
for schritte in pfad_zurueck:
    if schritte == "d":
        alignment[0] += sequence1[iterator1]
        alignment[1] += sequence2[iterator2]
        if sequence1[iterator1] == sequence2[iterator2]:
            alignment[2] += "*"
        else:
            alignment[2] += " "
        iterator1 += 1
        iterator2 += 1
    elif schritte == "unten":
        alignment[0] += sequence1[iterator1]
        alignment[1] += "-"
        alignment[2] += " "
        iterator1 += 1
    elif schritte == "r":
        alignment[0] += "-"
        alignment[1] += sequence2[iterator2]
        alignment[2] += " "
        iterator2 += 1


print(scor_wert[len(sequence1)][len(sequence2)], file=sys.stderr)
ausgabe_sequence1 = SeqIO.SeqRecord(Seq(alignment[0], generic_dna), ID1)
ausgabe_sequence2 = SeqIO.SeqRecord(Seq(alignment[1], generic_dna), ID2)
ausgabe_sequence3 = SeqIO.SeqRecord(Seq(alignment[2]), "")

ausgabe = [ausgabe_sequence1, ausgabe_sequence2, ausgabe_sequence3]

SeqIO.write(ausgabe, sys.stdout, "clustal")