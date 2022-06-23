import os
import ast
import numpy as np
from grafo import Grafo
from utils import minimum_spanning_tree

def prim(grafo, r=1):
    A = np.full(grafo.qtdVertices(), np.nan)

    K = np.full(grafo.qtdVertices(), np.inf)
    K[r-1] = 0

    Q = list(grafo.vertices.keys())
    while len(Q) > 0:
        #arg min
        valor_min = np.inf
        for vertice in Q:
            if K[vertice-1] < valor_min:
                u = vertice
                valor_min = K[vertice-1]

        Q.remove(u)

        for vizinho in grafo.vizinhos(u):
            peso_aresta = grafo.peso(u, vizinho)
            if vizinho in Q and peso_aresta < K[vizinho -1]:
                A[vizinho - 1] = u
                K[vizinho - 1] = peso_aresta

    vertices = list(grafo.vertices.keys())
    vertices.remove(r)
    arestas_ordenadas = []
    for v in vertices:
        aux = (v, int(A[v-1]))
        if aux in grafo.arestas:
            arestas_ordenadas.append(aux)
        else:
            arestas_ordenadas.append((int(A[v-1]), v))

    somatorio_pesos = 0
    for aresta in arestas_ordenadas:
        somatorio_pesos += grafo.peso(aresta[0], aresta[1])

    return arestas_ordenadas, somatorio_pesos

if __name__ == '__main__':
    arquivo = os.path.join('arquivos', 'agm_tiny.net')
    nao_dirigido = True
    grafo = Grafo(arquivo, nao_dirigido)
    A, somatorio_pesos = prim(grafo)
    minimum_spanning_tree(A, somatorio_pesos)