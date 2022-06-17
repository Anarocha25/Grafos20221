import os
import ast
import numpy as np
from grafo import Grafo

def prim(grafo):
    r = 1

    A = np.full(grafo.qtdVertices(), np.nan)

    K = np.full(grafo.qtdVertices(), np.inf)

    K[r-1] = 0

    Q = list(grafo.vertices.keys())

    while len(Q) > 0:
        #arg min
        valor_max = np.inf
        for vertice in Q:
            if K[vertice-1] < valor_max:
                u = vertice
                valor_max = K[vertice-1]

        #if u in Q:  
        Q.remove(u)

        for vizinho in grafo.vizinhos(u):
            peso_aresta = grafo.peso(u, vizinho)
            if vizinho in Q and peso_aresta < K[vizinho -1]:
                A[vizinho - 1] = u
                K[vizinho - 1] = peso_aresta
    return A

if __name__ == '__main__':
    arquivo = os.path.join('arquivos', 'agm_tiny.net')
    nao_dirigido = True
    grafo = Grafo(arquivo, nao_dirigido)
    A = prim(grafo)
    print("cy")