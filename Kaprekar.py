import numpy as np
import itertools
# import re

def to_Kaprekar(num: str, base: int = 10, length: int = -1, history: set = {}) -> int:

    num = str(num)
    if length == -1:
        length = len(num)

    if base == 10:
        need_history = length >= 5 or length == 2
    else:
        need_history = True

    # print(length)
    if not one_different(num, length - 1):
        # print('Conditions not met.')
        return -1

    # print(length)
    if need_history and type(history) == type({}):
        # print('a')
        history = {num}
    elif need_history and num in history:
        # print('b')
        # print(f'c: {num}')
        return 0
    elif need_history:
        # print(num)
        history.add(num)


    # print(f'a: {num}')    
    # print(history)
    # print(len(str(num)))
    # print(f'a: {length}')
    if len(num) == length - 1:
        num += '0'
    # print(f'a: {num}')
    # print(re.sub(r'[A-Z]', ' ', re.sub(r'\d', '0', num)))
    ordered_num = order(num)
    # print(f'd: {ordered_num}')
    # print(ordered_num)
    reverse = ordered_num[::-1]
    # print(f'e: {reverse}')
    difference = subtract_bases(ordered_num, reverse, base)
    # print(f'a: {type(num)}')
    # print(f'f: {type(difference)}')
    if not difference == num:
        return to_Kaprekar(difference, base, length, history) + 1
    else:
        print(f'b: {difference}')
        return 0

def order(num: str) -> list[str]:
    input_list = list(num)
    letter_list = []
    digit_list = []
    for i, digit in enumerate(input_list):
        if digit.isalpha():
            letter_list += input_list[i]
        else:
            digit_list += input_list[i]
        # else:
        #     print(f'h: {digit}')

    digit_list.sort(reverse = True)
    letter_list.sort(reverse = True)
    # print(f'g: {letter_list}')
    result = ''.join(letter_list) + ''.join(digit_list)
    return result

def one_different(num: str, length: int = 3) -> bool:
    if len(num) == length:
        return True
    for digit1 in list(num):
        for digit2 in list(num):
            if not digit1 == digit2:
                return True
    return False

def average_steps(base: int = 10, digit_count: int = 4) -> int:
    total_steps = 0
    count = 0
    # for i in range(10 ** (digit_count - 1), 10 ** (digit_count)):
    for i in itertools.count():
        base_i = np.base_repr(i, base)
        if len(base_i) < digit_count:
            # print(f'{i}, {base_i}')
            continue
        elif len(base_i) == digit_count:
            # print(f'{i}. {base_i}')
            steps = to_Kaprekar(base_i, base)
            total_steps += steps
            if steps > -1:
                count += 1
        else:
            break

    average = total_steps / count
    return average

def subtract_bases(num1: str, num2: str, base: int = 10) -> str:
    if base == 10:
        return str(int(num1) - int(num2))
    else:
        num1, num2 = [int(num, base) for num in [num1, num2]]
        # print(f'g: {num1, num2}')
        result = num1 - num2
        return np.base_repr(result, base)

# print(to_Kaprekar('67843876', 10))
# print(one_different(1110))

# print(subtract_bases('E', 'C', 16))

print(average_steps(9, 2))

# base 27: 5
# base 2: 4-7

# print(to_Kaprekar('ABCDEFGHIJKLMNO2939489585', 36))

