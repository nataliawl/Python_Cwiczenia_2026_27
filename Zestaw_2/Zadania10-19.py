from unittest import result


def count_words_in_line_10(line: str) -> int:
    return len(line.split())

def separate_chars_11(word: str) -> str:
    new_word = list(word)
    return '_'.join(new_word)

def first_char_in_words_12(line: str) -> str:
    words = line.split()
    first_char_list = []
    for word in words:
        first_char_list.append(word[0])
    return "".join(first_char_list)

def last_char_in_words_12(line: str) -> str:
    words = line.split()
    last_chars_list = []
    for word in words:
        last_chars_list.append(word[len(word) - 1])

    return "".join(last_chars_list)

def sum_words_lenght_13(line: str) -> int:
    words = line.split()
    words_lenght = 0
    for word in words:
        words_lenght += len(word)
    return words_lenght

def longest_word_14(line: str):
    words = line.split()
    longest_word = ''
    word_lenght = 0
    for word in words:
        if len(word) > word_lenght:
            longest_word = word
            word_lenght = len(word)

    print(longest_word)
    longest_word_lenght = len(longest_word)
    return longest_word, longest_word_lenght

def numbers_to_string_15(L : list) -> str:
    list_str = ''
    for numb in L:
        list_str += str(numb)
    return ''.join(list_str)

def change_word_in_line_16(line: str) -> str:
    check_line = line.split()
    for idx in range(len(check_line)):
        if check_line[idx] == 'GvR':
            check_line[idx] = 'Guido van Rossum'
    return " ".join(check_line)

def sort_alfabeticaly_17(line: str) -> list[str]:
    lower_line = line.lower()
    alfa_list = lower_line.split()
    print(sorted(alfa_list))
    return sorted(alfa_list)

def sort_by_lenght_17(line: str) -> list[str]:
    lower_line = line.lower()
    alfa_list = lower_line.split()
    alfa_list.sort()
    print(sorted(alfa_list,key=len))
    return sorted(alfa_list, key = len)

def count_zeroes_18(numb : int) -> int:
    zeroes = 0
    str_num = str(numb)
    for char in str_num:
        if char == '0':
            zeroes += 1

    return zeroes

def fill_string_with_zeroes_19(L: list) -> str:
    list_str = ''
    for numb in L:
        list_str += str(numb).zfill(3) + " "

    return list_str

if __name__ == '__main__':
    #Zmienne na dzialaniach na funkcjach
    line = """Litwo, Ojczyzno moja! ty jestes jak zdrowie
    Ile cie trzeba cenic, ten tylko sie dowie,
    Kto cie stracil. Dzis pieknosc twa w calej ozdobie
    Widze i opisuje, bo tesknie po tobie."""
    word = "dynia" #d_y_n_i_a
    L = [0, 5, 6, 1, 22, 100]
    number = 120200200
    test_GVR = "To jest test GvR ma zmienic GvR"

    #Spodziewane odpowiedzi
    expected_answer_10 = 31
    expected_answer_11 = "d_y_n_i_a"
    first_chars_12 = "LOmtjjzIctcttsdKcsDptwcoWiobtpt"
    last_chars_12 = ",o!yskeeea,noe,oe.scawjeei,oeo."
    expected_answer_13 = 145
    longest_word_lenght_14 = 8
    longest_word_check_14 = "Ojczyzno"
    expected_answer_15 = "056122100"
    expected_answer_16 = "To jest test Guido van Rossum ma zmienic Guido van Rossum"
    alfa_expected_answer_17 = ['bo', 'calej', 'cenic,', 'cie', 'cie', 'dowie,', 'dzis', 'i', 'ile', 'jak', 'jestes', 'kto', 'litwo,', 'moja!', 'ojczyzno', 'opisuje,', 'ozdobie', 'pieknosc', 'po', 'sie', 'stracil.', 'ten', 'tesknie', 'tobie.', 'trzeba', 'twa', 'ty', 'tylko', 'w', 'widze', 'zdrowie']
    lenght_expected_answer_17 = ['i', 'w', 'bo', 'po', 'ty', 'cie', 'cie', 'ile', 'jak', 'kto', 'sie', 'ten', 'twa', 'dzis', 'calej', 'moja!', 'tylko', 'widze', 'cenic,', 'dowie,', 'jestes', 'litwo,', 'tobie.', 'trzeba', 'ozdobie', 'tesknie', 'zdrowie', 'ojczyzno', 'opisuje,', 'pieknosc', 'stracil.']
    expected_answer_18 = 5
    expected_answer_19 = "000 005 006 001 022 100 "

    #Testy
    assert count_words_in_line_10(line) == expected_answer_10
    assert separate_chars_11(word) == expected_answer_11
    assert first_char_in_words_12(line) == first_chars_12
    assert last_char_in_words_12(line) == last_chars_12
    assert sum_words_lenght_13(line) == expected_answer_13
    answer_14, answer_14_lenght = longest_word_14(line)
    assert answer_14 == longest_word_check_14
    assert answer_14_lenght == longest_word_lenght_14
    assert numbers_to_string_15(L) == expected_answer_15
    assert change_word_in_line_16(test_GVR) == expected_answer_16
    assert sort_alfabeticaly_17(line) == alfa_expected_answer_17
    assert sort_by_lenght_17(line) == lenght_expected_answer_17
    assert count_zeroes_18(number) == expected_answer_18
    assert fill_string_with_zeroes_19(L) == expected_answer_19


