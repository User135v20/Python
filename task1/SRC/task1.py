import re
def converter(**kwargs):
    print(type())
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

def converter_to_10(input_str: list,system: list):
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

def valid_10_number(input_number: str):
    L = len(input_number)
    if input_number[0] == '0' and L > 1:
        return False
    pattern = '\d' + r'{'+ r'{}'.format(L)+r'}'
    result = re.search(pattern, input_number)
    if not result:
        return False
    return True

def valid_system(input_system):
    L = len(input_system)
    if L == 1:
        return False
    for i in range(L):
        for j in range(i+1,L):
            if input_system[i] == input_system[j]:
                return False
    return True
def valid_num_from_any_system(input_num,input_system):
    for el in input_num:
        if not el in input_system:
            return False
    return True

def main():
    num = (input()) #Введите число в 10-чной системе счисления:
    system = list(input()) #"Введите систему счисления: "
    if valid_system(system)*valid_10_number(num) == True:
        num = int(num)
        result = converter_from_10(num, system)
        print(*result)
    else: print("usage")

    Y = input('подолжить введите "Y", выйти другой символ и enter: ')
    if Y == "Y":
        #print("Введите сначала число, потом его систему счисления и систему счисления для перевода")
        Num = list(input())
        system1 = list(input())
        system2 = list(input())
        if valid_system(system1)*valid_system(system2)*valid_num_from_any_system(Num,system1):
            a = (converter_to_10(Num,system1))
            a = converter_from_10(a,system2)
            print(*a)
        else:print('usage')

if __name__ == '__main__':
    main()