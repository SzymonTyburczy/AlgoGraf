from dimacs import *
from typing import Tuple
import os
from pathlib import Path
from time import time

# Tu importujemy sobie funkcję sol
from lab3_main import None as tested_solution

V: int
L: Tuple[int, int, int]

# Sciezka do folderu w którym są testy (działa o ile w podanym na końcu katalogu są tylko testy)
# Całe rozwiązanie dajemy jako funkcję def solution(dir):
# i na jej końcu doklejamy print(sol, nasz_wynik, int(sol) == int(naszw_wynik))
# wypiszą się kolejne testy i ich rezultat
tests_path = "."
ignored_file = "grid100x100"

print(os.listdir(tests_path))
files = [
    os.path.join(tests_path, f)
    for f in os.listdir(tests_path)
    if os.path.isfile(os.path.join(tests_path, f)) and f != ignored_file
]

# print(files)

for test in files:
    t0 = time()
    print(test)
    (V, L) = loadWeightedGraph(test)
    expected = readSolution(test)
    real = tested_solution(L, V, 1, V)
    print(real, expected)
    print(int(real) == int(expected))
    t1 = time()
    print("czas wykonania {ex_time:.4f} s\n".format(ex_time=t1 - t0))
