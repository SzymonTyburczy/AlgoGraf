# wyszukiwanie binarne + przeglad grafu metodami BFS/DFS
# zmieniamy z problemu optymalizacyjnego na problem decyzyjny  (jak najwiekszy ) -> (dla danej wagi pojazdu czy jest w stanie dojechac czy nie)
# mamy jakies auto i jedziemy nim dfsem albo bfsem tylko jesli wartosc krawedzi pozwala na jego przejazd
from dimacs import *
from queue import Queue
from math import inf

# Wczytaj graf z pliku (wierzchołki ponumerowane od 1 do V)
(V, L) = loadWeightedGraph("graphs-lab1/g1")
G = [set() for _ in range(V)]

# Przekształcenie wierzchołków na indeksy od 0
for u, v, c in L:
    u -= 1
    v -= 1
    G[u].add((v, c))
    G[v].add((u, c))


# DFS sprawdzający, czy da się przejechać z wierzchołka start do end, używając tylko krawędzi o wagach >= min_waga
def dfs(G, start, end, min_waga):
    visited = [False] * len(G)

    def rek(v):
        visited[v] = True
        if v == end:
            return True
        for neighbour, waga in G[v]:
            if not visited[neighbour] and waga >= min_waga:
                if rek(neighbour):
                    return True
        return False

    return rek(start)


# BFS sprawdzający, czy da się przejechać z wierzchołka start do end, używając tylko krawędzi o wagach >= min_waga
# def bfs(G, start, end, min_waga):
#     visited = [False] * len(G)
#     visited[start] = True
#     Q = Queue()
#     Q.put(start)
#
#     while not Q.empty():
#         v = Q.get()
#         if v == end:
#             return True
#         for neighbour, waga in G[v]:
#             if not visited[neighbour] and waga >= min_waga:
#                 visited[neighbour] = True
#                 Q.put(neighbour)
#
#     return False


# Funkcja szukająca maksymalnej wagi krawędzi, która pozwala przejechać z start do end
def bin_search_max_waga(G, start, end, minimalna_waga, maksymalna_waga):
    left, right = minimalna_waga, maksymalna_waga

    while left <= right:
        mid = (left + right) // 2

        # Sprawdzamy, czy można przejechać dla danej wagi pojazdu (używając DFS lub BFS)
        if dfs(G, start, end, mid):  # Możesz zamienić bfs na dfs, jeśli wolisz
            left = mid + 1  # Jeżeli można przejechać, próbujemy większą wagę
        else:
            right = mid - 1  # Jeżeli nie można, zmniejszamy wagę

    return right  # Zwracamy maksymalną wagę, dla której można przejechać


# Szukanie minimalnej i maksymalnej wagi krawędzi w grafie
minimalna_waga = inf
maksymalna_waga = -1

for sasiedzi in G:
    for wierzcholek, waga in sasiedzi:
        minimalna_waga = min(minimalna_waga, waga)
        maksymalna_waga = max(maksymalna_waga, waga)

# Szukamy maksymalnej wagi krawędzi, która pozwala przejechać z wierzchołka 0 do 1
print(bin_search_max_waga(G, 0, 1, minimalna_waga, maksymalna_waga))
