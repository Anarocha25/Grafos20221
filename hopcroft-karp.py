from pydoc import doc
import numpy as np
import os
from grafo import Grafo
from queue import Queue

def hopcroft_karp(grafo: Grafo):
    grafo.X = {v[0] for v in grafo.arestas}
    grafo.Y = {v[1] for v in grafo.arestas}

    D = {v: np.inf for v in grafo.vertices}
    mate = {v: None for v in grafo.vertices}
    m = 0
    while BFS(grafo, mate, D):
        for x in grafo.X:
            if mate[x] is None:
                if DFS(grafo, mate, x, D):
                    m += 1

    return m, mate

def BFS(grafo: Grafo, mate, D):
    Q = Queue()

    for x in grafo.X:
        if mate[x] is None:
            D[x] = 0
            Q.put(x)
        else:
            D[x] = np.inf

    D[None] = np.inf
    while not Q.empty():
        x = Q.get()
        if D[x] < D[None]:
            for y in grafo.vizinhos(x):
                if D[mate[y]] == np.inf:
                    D[mate[y]] = D[x] + 1
                    Q.put(mate[y])

    return D[None] != np.inf

def DFS(grafo: Grafo, mate, x, D):
    if x is not None:
        for y in grafo.vizinhos(x):
            if D[mate[y]] == D[x] + 1:
                if DFS(grafo, mate, mate[y], D):
                    mate[y] = x
                    mate[x] = y
                    return True
        D[x] = np.inf
        return False
    return True


if __name__ == '__main__':
    arquivo = os.path.join('arquivos', 'emparelhamento.net')
    grafo = Grafo(arquivo)

    emparelhamento = hopcroft_karp(grafo)
    print(f"Emparelhamento maximo: {emparelhamento[0]}")
    print(f"Emparelhamentos: {emparelhamento[1]}")
