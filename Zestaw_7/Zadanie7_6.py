import itertools
import random
#Stworzyć następujące iteratory nieskończone:

#(a) zwracający 0, 1, 0, 1, 0, 1, ...,
iter_binary = itertools.cycle([0, 1])

#(b) zwracający przypadkowo jedną wartość z ("N", "E", "S", "W") [błądzenie przypadkowe na sieci kwadratowej 2D],
iter_map = iter(lambda: random.choice(["N", "E", "S", "W"]), -1)

#(c) zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... [numery dni tygodnia].
iter_week = itertools.cycle(range(7))
