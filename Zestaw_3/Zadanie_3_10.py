def is_float(value : str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False

def print_for_3 (num:int) -> str:
    number_list = []
    for i in range(num + 1):
        if i%3 == 0:
            continue
        number_list.append(str(i))
    return ' '.join(number_list)

def print_while_3 (num:int) -> str:
    number_list = []
    i = -1
    while i < num:
        i += 1
        if i%3 == 0:
            continue
        number_list.append(str(i))
    return ' '.join(number_list)

def third_power_4():
    while True:
        print("Aby zatrzymac program napisz 'stop' ")
        numb = input("Podaj liczbe: ")
        if numb == 'stop':
            print("Zatrzymanie programu")
            break
        if is_float(numb):
            float_numb = float(numb)
            print("Podano liczbe: " + numb)
            print("Trzecia potega liczby " + numb + " to: " + str(float_numb ** 3))
        else:
            print("Blad : napis nie moze byc spotegowany")
            continue

def create_ruler_5(ruler_lenght : int, lines_number = 4) -> str:
    ruler = ''

    for i in range(ruler_lenght + 1):
        ruler += '|'
        if i < ruler_lenght:
            for j in range(lines_number):
                ruler += '-'

    ruler += '\n0'

    for i in range(1, ruler_lenght + 1):
        for j in range(lines_number - len(str(i)) + 1):
            ruler += ' '
        ruler += str(i)

    print(ruler)

    return ruler

def create_rectangle_of_small_squares_6(x: int, y: int) -> str:
    rectangle = ''
    if x == 0 or y == 0:
        print("Zmienne musza byc wieksze od 0!")
        return rectangle
    end_y = 0
    while True:
        rectangle += '+'
        for i in range(x):
            rectangle += '---+'
        if end_y == y:
            break
        rectangle += '\n|'
        for j in range(x):
            rectangle += '   |'
        rectangle += '\n'
        end_y += 1
    print(rectangle)
    return rectangle

def find_doubles_characters_8(string_1: str, string_2: str) -> list[str]:
    doubles_characters = []
    for char_1 in string_1:
        if char_1 in string_2 and char_1 not in doubles_characters:
            doubles_characters.append(char_1)

    return doubles_characters

def list_of_characters_8(string_1: str, string_2: str) -> list[str]:
    list_of_characters = []
    for char_1 in string_1:
        if char_1 not in list_of_characters:
            list_of_characters.append(char_1)
    for char_2 in string_2:
        if char_2 not in list_of_characters:
            list_of_characters.append(char_2)

    return list_of_characters

def sum_of_lists_9(list_of_lists: list[list[int]] | list[tuple[int]]) -> list[int]:
    list_of_sums = []

    for list_numbs in list_of_lists:
        list_of_sums.append(sum(list_numbs))

    return list_of_sums

def roman2int_10(roman_numb: str) -> int:
    roman_to_arabic = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    # Można też zanaicjalizować pusty słownik i dodawać klucze:
    # roman_to_arabic = {}
    # roman_to_arabic['I'] = 1
    # itd.

    # Można także dokonać konwersji krotek do słownika:
    # roman_to_arabic = dict([("I", 1), ("V", 5),
    # ("X", 10), ("L", 50), ("C", 100), ("D", 500), ("M", 1000)])

    # Z dwóch listy:
    # roman_to_arabic = dict(zip(["I", "V", "M"], [1, 5,1000]))

    arabic_numb = 0;
    roman_numb = roman_numb.replace("IV", "IIII").replace("IX", "VIIII")
    roman_numb = roman_numb.replace("XL", "XXXX").replace("XC", "LXXXX")
    roman_numb = roman_numb.replace("CD", "CCCC").replace("CM", "DCCCC")

    for numb in roman_numb:
        arabic_numb += roman_to_arabic[numb]
    return arabic_numb

if __name__ == '__main__':
    test_list = [[],[4],(1,2),[3,4],(5,6,7)]
    test_string_1 = "axxx56:q"
    test_string_2 = "xeee6:!!bb"

    expected_answer_3 = "1 2 4 5 7 8 10 11 13 14 16 17 19 20 22 23 25 26 28 29"
    expected_answer_5 = """|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
0    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26   27   28   29   30   31   32   33   34   35   36   37   38   39   40   41   42   43   44   45   46   47   48   49   50   51   52   53   54   55   56   57   58   59   60   61   62   63   64   65   66   67   68   69   70   71   72   73   74   75   76   77   78   79   80   81   82   83   84   85   86   87   88   89   90   91   92   93   94   95   96   97   98   99  100"""
    expected_answer_6 = """+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+"""
    expected_answer_8_1 = ['x', '6', ':']
    expected_answer_8_2 = ['a','x', '5', '6', ':', 'q', 'e', '!', 'b']
    expected_answer_9 = [0,4,3,7,18]
    expected_answer_10 = 1416

    assert print_for_3(30) == expected_answer_3
    assert print_while_3(30) == expected_answer_3
    assert create_ruler_5(100) == expected_answer_5
    assert create_rectangle_of_small_squares_6(4, 2) == expected_answer_6
    assert find_doubles_characters_8(test_string_1, test_string_2) == expected_answer_8_1
    assert list_of_characters_8(test_string_1, test_string_2) == expected_answer_8_2
    assert expected_answer_9 == sum_of_lists_9(test_list)
    assert roman2int_10("MCDXVI") == expected_answer_10

    third_power_4()

