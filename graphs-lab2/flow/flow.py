import dimacs as dim
from math import inf
# szukamy przeplywow miedzy pierwszym i ostatnim wierzcholkiem
(V, L) = dim.loadDirectedWeightedGraph("clique5")


def lista_sasiadow(Graph, max_vertex):
    # lista sasiedztwa przy czym [0] -dla pierwszego wierzcholka
    Neigh_list = [[] for _ in range(max_vertex)]
    Neight_list2 = [[] for _ in range(max_vertex)]
    for v, w, p in Graph:
        Neigh_list[w - 1].append((v, 0, p))
        Neigh_list[v - 1].append((w, 0, p))
    return Neigh_list, Neight_list2


def dfs(G, start, end):
    visited = [False] * len(G)
    nonlocal min_capacity
    min_capacity = inf
    def rek(v, min_capacity):
        visited[v] = True
        if v == end:
            return min_capacity
        for neighbour, flow, max_cap in G[v]:
            min_capacity = min(min_capacity, max_cap)
            if not visited[neighbour]:
                if rek(neighbour):
                    return True
        return False

    return rek(start)



def Ford_Fulkerson(Graph, start, finish):
    dfs(Graph, start, finish)


