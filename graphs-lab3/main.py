#implementacja reprezentacji grafu oraz jego wczytywanie
from dimacs import *
(V, L) = loadWeightedGraph("clique5") #Count(Vertices), Graph
for x, y, c in L:
    print(x, y, c) #v1, v2, weight
def mtn(G, V):
    L = [[] for _ in range(V + 1)]
    for i in range(len(G)):
        L[G[i][0]].append((G[i][1], G[i][2]))
        L[G[i][1]].append((G[i][0], G[i][2]))
    return L

print(mtn(L, V))
#scalanie wierzcholkow

def merge_verticies():
    

