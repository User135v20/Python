def converter_from_10(number, number_system):
    bit_depth = len(number_system)
    result = []
    while number > 0:
        remains = number % bit_depth
        number = number // bit_depth
        result.append(number_system[remains])
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

def main():
    num = int(input("Введите число в 10-чной системе счисления: "))
    system = list(input("Введите систему счисления: "))

    #system = [0, 1, 2, 3, 4,5,6,7,8,9,'a','b','c','d','e','f']
    system2 = [0,1,2]
    print(converter_from_10(num, system)) # число в 10чной потом систему счисления листом
    Y = input('чтобы подолжить введите "Y", чтобы выйти другой символ и enter: ')
    if Y == "Y":
        print(converter_to_10([2,2,2],system2))
        #сначала число в виде листа потом лист с ситемой из которой переводить в 10 чную

if __name__ == '__main__':
    main()