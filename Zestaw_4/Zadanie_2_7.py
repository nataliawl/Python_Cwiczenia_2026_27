def make_ruler_2(n : int, lines_number = 4) -> str:
    if n <= 0 or lines_number <= 0:
        raise ValueError("Zmienne musza byc wieksze od 0!")

    ruler = ''
    for i in range(n + 1):
        ruler += '|'
        if i < n:
            for j in range(lines_number):
                ruler += '-'

    ruler += '\n0'

    for i in range(1, n + 1):
        for j in range(lines_number - len(str(i)) + 1):
            ruler += ' '
        ruler += str(i)

    return ruler

def make_grid_2(rows: int, cols: int) -> str:
    if rows <= 0 or cols <= 0:
        raise ValueError("Zmienne musza byc wieksze od 0!")
    rectangle = ''
    end_y = 0
    while True:
        rectangle += '+'
        for i in range(rows):
            rectangle += '---+'
        if end_y == cols:
            break
        rectangle += '\n|'
        for j in range(rows):
            rectangle += '   |'
        rectangle += '\n'
        end_y += 1

    return rectangle

def factorial_3(n: int) -> int:
    if n < 0:
        raise ValueError("Zmienne nie moga byc ujemne!")
    if n == 0: return 1

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

def fibonacci_4(n: int) -> int:
    if n < 0:
        raise ValueError("Zmienne nie moga byc ujemne!")
    if n == 0:
        return 0
    before = 0
    result = 1
    for i in range(n - 1):
        old_result = result
        result = old_result + before
        before = old_result
    return result

def odwracanie_5_ite(L : list, left : int, right: int) -> list:
    if left < 0 or right < 0:
        raise ValueError("Zmienne nie moga byc ujemne!")
    while left < right:
        pom = L[left]
        L[left] = L[right]
        L[right] = pom
        left += 1
        right -= 1

    return L

def odwracanie_5_re(L : list, left : int, right: int) -> list:
    if left < 0 or right < 0:
        raise ValueError("Zmienne nie moga byc ujemne!")
    if left >= right:
        return L
    pom = L[left]
    L[left] = L[right]
    L[right] = pom
    odwracanie_5_re(L, left + 1, right - 1)
    return L

def sum_seq_6(sequence : list | tuple) -> float:
    seq_sum = 0
    for element in sequence:
        if isinstance(element, (tuple, list)):
            seq_sum += sum_seq_6(element)
        else:
            seq_sum += element
    return seq_sum

def flatten_7(sequence: list | tuple) -> list:
    seq_list = []
    for element in sequence:
        if isinstance(element, (tuple, list)):
            seq_list.extend(flatten_7(element))
        else:
            seq_list.append(element)

    return seq_list

if __name__ == '__main__':
    test_list_5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    test_list_6= [0, (1, 2), 4, [3, 4], (5, 6, 7)]
    test_list_7= [1,(2,3),[],[4,(5,6,7)],8,[9]]

    expected_answer_2_ruler= """|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
0    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26   27   28   29   30   31   32   33   34   35   36   37   38   39   40   41   42   43   44   45   46   47   48   49   50   51   52   53   54   55   56   57   58   59   60   61   62   63   64   65   66   67   68   69   70   71   72   73   74   75   76   77   78   79   80   81   82   83   84   85   86   87   88   89   90   91   92   93   94   95   96   97   98   99  100"""
    expected_answer_2_grid = """+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+"""
    expected_answer_3 = 3628800
    expected_answer_4 = 2584
    expected_answer_5_even = [1, 2, 6, 5, 4, 3, 7, 8, 9, 10]
    expected_answer_5_odd = [1, 2, 5, 4, 3, 6, 7, 8, 9, 10]
    expected_answer_6 = 32
    expected_answer_7 = [1,2,3,4,5,6,7,8,9]

    assert make_ruler_2(100) == expected_answer_2_ruler
    assert make_grid_2(4, 2) == expected_answer_2_grid
    assert factorial_3(10) == expected_answer_3
    assert fibonacci_4(18) == expected_answer_4
    test_list_5_copy = test_list_5.copy()
    assert odwracanie_5_ite(test_list_5_copy, 2, 5) == expected_answer_5_even
    test_list_5_copy = test_list_5.copy()
    assert odwracanie_5_ite(test_list_5_copy, 2, 4) == expected_answer_5_odd
    test_list_5_copy = test_list_5.copy()
    assert odwracanie_5_re(test_list_5_copy, 2, 5) == expected_answer_5_even
    test_list_5_copy = test_list_5.copy()
    assert odwracanie_5_re(test_list_5_copy, 2, 4) == expected_answer_5_odd
    assert sum_seq_6(test_list_6) == expected_answer_6
    assert flatten_7(test_list_7) == expected_answer_7