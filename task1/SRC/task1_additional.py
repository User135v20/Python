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


def converter_to_10(input_str: list, system: list):
    bit_depth = len(system)
    k = len(input_str)
    result = 0
    for i in range(k):
        if input_str[k - i - 1] != 0:
            sum = bit_depth ** i * system.index(input_str[k - i - 1])
        else:
            continue
        result = result + sum
    return result


def valid_system(input_system):
    L = len(input_system)
    if L == 1:
        return False
    for i in range(L):
        for j in range(i + 1, L):
            if input_system[i] == input_system[j]:
                return False
    return True


def valid_num_from_any_system(input_num, input_system):
    for el in input_num:
        if el not in input_system:
            return False
    return True


def main(num, system1, system2):
    # print("Введите сначала число, потом его систему счисления и систему счисления для перевода")
    if valid_system(system1) * valid_system(system2) * valid_num_from_any_system(num, system1):
        result = (converter_to_10(num, system1))
        result = converter_from_10(result, system2)
        print(*result)
    else:
        print('usage')


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 4:
        main(args[1], args[2], args[3])
    else:
        print('usage')
    #ex python task1_additional.py 10101010 01 0123456789
