
def find_index(input_str=str, request_str=str, beginning=int):
    if request_str != '':
        ind = input_str.find(request_str,beginning)
        return ind+len(request_str)-1
    else:
        return -1

def main():
    begin = 0
    Flag_ = False
    Flag_KO = False
    first_str = input()
    second_str = input()
    request_str = second_str.split('*')
    for el in request_str:
        new_index = find_index(first_str, el, begin)
        if Flag_ == False and new_index != -1:
            if new_index - begin == len(el)-1:
                begin = new_index+1
            else:
                Flag_KO = True
                break
        elif Flag_ == True and new_index != -1:
            begin = new_index+1
        Flag_=True

    if Flag_KO == False and (el == '' or (el != '' and len(first_str)==begin)):
        print("OK")
    else:
        print("KO")

if __name__ == '__main__':
    main()