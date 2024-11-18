from dimacs import *
from queue import PriorityQueue
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


# Algorytm Dijkstry zmodyfikowany do maksymalizowania najmniejszej wagi na ścieżce
def Dijkstra(Graph, start, end):
    PQ = PriorityQueue()
    # Na początku każda ścieżka ma najmniejszą wagę równą -1 (brak ścieżki)
    best_min_edge = [-1 for _ in range(len(Graph))]
    visited = [False for _ in range(len(Graph))]

    # Startujemy od wierzchołka początkowego, gdzie najmniejsza krawędź wynosi inf
    best_min_edge[start] = inf
    PQ.put((-inf, start))  # Umieszczamy -inf, aby największy miał priorytet

    while not PQ.empty():
        min_edge_u, u = PQ.get()
        min_edge_u = -min_edge_u  # Oryginalna wartość minimalnej krawędzi na ścieżce do u

        if u == end:
            return min_edge_u  # Znaleźliśmy najlepszą ścieżkę do wierzchołka końcowego

        if visited[u]:
            continue

        visited[u] = True

        for v, weight in Graph[u]:
            # Nowa potencjalna minimalna krawędź na ścieżce do v
            new_min_edge = min(min_edge_u, weight)

            # Jeżeli nowa minimalna krawędź na ścieżce do v jest lepsza niż dotychczasowa
            if new_min_edge > best_min_edge[v]:
                best_min_edge[v] = new_min_edge
                PQ.put((-new_min_edge, v))  # Ujemna wartość, bo kolejka priorytetowa działa na zasadzie minimum

    return best_min_edge[end]  # Zwracamy najlepszą wartość dla wierzchołka końcowego


# Wierzchołki startowy i końcowy numerujemy od 0, czyli 1 -> 0, 2 -> 1
print(Dijkstra(G, 0, 1))
