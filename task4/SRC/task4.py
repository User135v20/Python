def find_index(input_str: str, request_str: str, beginning: int):
    ind = input_str.find(request_str, beginning)
    return ind + len(request_str) if ind != -1 else -1


def are_similar(first_str: str, second_str: str):
    need_check_first_symbol = True if second_str and second_str[0] != '*' else False
    need_check_last_symbol = True if second_str and second_str[-1] != '*' else False
    substrings = second_str.split('*')
    if len(substrings) == 1:
        return first_str == second_str
    substrings = [i for i in substrings if i]   # delete ''
    search_start_position = 0
    for desired_substring in substrings:
        new_index = find_index(first_str, desired_substring, search_start_position)
        if new_index == -1:
            return False
        if need_check_first_symbol is False or need_check_first_symbol and new_index - search_start_position == len(desired_substring):
            search_start_position = new_index
        else:
            return False
        need_check_first_symbol = False
    if need_check_last_symbol == True and new_index-1 < len(first_str): return False
    return True


def main():
    first_str = input()
    second_str = input()
    if are_similar(first_str, second_str):
        print("OK")
    else:
        print("KO")


if __name__ == '__main__':
    main()
