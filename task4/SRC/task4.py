import sys

def find_index(input_str: str, request_str: str, beginning: int):
    ind = input_str.find(request_str, beginning)
    return ind + len(request_str) if ind != -1 else -1

def are_similar(first_str: str, second_str: str):
    need_check_first_symbol = True if second_str and second_str[0] != '*' else False
    need_check_last_symbol = True if second_str and second_str[-1] != '*' else False
    substrings = second_str.split('*')
    if second_str.find('*') == -1:
        return first_str == second_str
    substrings = [i for i in substrings if i]   # delete ''
    if not substrings:
        return True
    search_start_position = 0
    substrings_ = substrings[:-1] if need_check_last_symbol else substrings
    for desired_substring in substrings_:
        new_index = find_index(first_str, desired_substring, search_start_position)
        if new_index == -1:
            return False
        if need_check_first_symbol is False or need_check_first_symbol and new_index - search_start_position == len(desired_substring):
            search_start_position = new_index
        else:
            return False
        need_check_first_symbol = False
    if need_check_last_symbol:
        ind_ = first_str.rfind(substrings[-1])
        if ind_ == -1:
            return False
        if ind_ + len(substrings[-1]) != len(first_str):
            return False
    return True

def main(first_str: str, second_str: str):

    #first_str = input()
   # second_str = input()
    if are_similar(first_str, second_str):
        print("OK")
    else:
        print("KO")

if __name__ == '__main__':
    args = sys.argv
    if len(args) == 3:
        main(args[1], args[2])
    else:
        print('KO')

