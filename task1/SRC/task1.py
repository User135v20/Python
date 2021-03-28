import re
import sys


def converter_from_10(number, number_system):
    bit_depth = len(number_system)
    result = []
    if number > 0:
        while number > 0:
            remains = number % bit_depth
            number = number // bit_depth
            result.append(number_system[remains])
    elif number == 0:
        result.append(number_system[0])
    result.reverse()
    return result


def valid_10_number(input_number: str):
    l = len(input_number)
    if input_number[0] == '0' and l > 1:
        return False
    pattern = '\d' + r'{' + r'{}'.format(l)+r'}'
    result = re.search(pattern, input_number)
    if not result:
        return False
    return True


def valid_system(input_system):
    l = len(input_system)
    if l == 1:
        return False
    for i in range(l):
        for j in range(i+1, l):
            if input_system[i] == input_system[j]:
                return False
    return True


def valid_num_from_any_system(input_num, input_system):
    for el in input_num:
        if el not in input_system:
            return False
    return True


def main(num: str, system: str):
    #num = (input()) #Введите число в 10-чной системе счисления:
    #system = list(input()) #"Введите систему счисления: "
    if valid_system(list(system))*valid_10_number(num) == True:
        num = int(num)
        result = converter_from_10(num, system)
        print(*result)
    else:
        print("usage")


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 3:
        main(args[1], args[2])
    else:
        print('usage')

    # ex python task1.py 1010 01