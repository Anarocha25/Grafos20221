import os
import numpy as np
from grafo import Grafo
import copy


def ordenacao(grafo: Grafo):
    C = {vertice: False for vertice in grafo.vertices}
    T = {vertice: np.inf for vertice in grafo.vertices}
    F = {vertice: np.inf for vertice in grafo.vertices}

    tempo = [0]

    O = []

    for u in grafo.vertices:
        if C[u] is False:
            DFS_visit_OT(grafo, u, C, T, F, tempo, O)

    return O


def DFS_visit_OT(grafo: Grafo, v, C, T, F, tempo, O):
    C[v] = True
    tempo[0] += 1
    T[v] = tempo[0]

    for u in grafo.vizinhos(v):
        if C[u] is False:
            DFS_visit_OT(grafo, u, C, T, F, tempo, O)

    tempo[0] += 1
    F[v] = tempo[0]
    O.insert(0, v)


if __name__ == '__main__':
    arquivo = os.path.join('arquivos', 'manha.net')
    grafo = Grafo(arquivo, nao_dirigido=False)
    O = ordenacao(grafo)

    named_O = []
    for i in O:
        named_O.append(grafo.vertices[i])

    print(" -> ".join(named_O))
