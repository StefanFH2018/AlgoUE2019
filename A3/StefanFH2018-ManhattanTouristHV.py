#!/usr/bin/python3

import sys

file_input = sys.stdin.readlines()


def float_list(list_input):
    float_conv_list = []
    for line in list_input:
        new_row = []
        for item in line:
            new_row.append(float(item))
        float_conv_list.append(new_row)
    return float_conv_list


down_matrix = []
right_matrix = []

bin_ich_in_right_matrix = False
bin_ich_in_down_matrix = False

for line_input in file_input:
    line_input.strip("\n")
    if "G_down" in line_input:
        bin_ich_in_down_matrix = True
        continue
    elif "G_right" in line_input:
        bin_ich_in_right_matrix = True
        continue
    elif "---" in line_input:
        bin_ich_in_down_matrix = bin_ich_in_right_matrix = False
        continue

    if bin_ich_in_down_matrix == True:
        down_matrix.append(line_input.split())

    elif bin_ich_in_right_matrix == True:
        right_matrix.append(line_input.split())

down_matrix = float_list(down_matrix)
right_matrix = float_list(right_matrix)

length_column = len(down_matrix[1])
length_line = len(right_matrix)

calculation_list = []
line_1 = [0]

for i in range(1, length_column, 1):
    line_1.append(line_1[i - 1] + right_matrix[0][i - 1])
calculation_list.append(line_1)

for line in range(1, length_line, 1):
    calculation_list.append([calculation_list[line - 1][0] + down_matrix[line - 1][0]])
    for column in range(1, length_column, 1):
        vertical = calculation_list[line - 1][column] + down_matrix[line - 1][column]
        horizontal = calculation_list[line][column - 1] + right_matrix[line][column - 1]
        if horizontal >= vertical:
            calculation_list[line].append(horizontal)
        elif vertical > horizontal:
            calculation_list[line].append(vertical)

print(calculation_list[length_column - 1][length_line - 1])

