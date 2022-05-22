import numpy as np
from grafo import GrafoNaoDirigido
from utils import print_ex_4

def bellman_ford(grafo: GrafoNaoDirigido, vertice_inicial: int):
    D = {vertice: np.inf for vertice in grafo.vertices}
    A = {vertice: None for vertice in grafo.vertices}
    D[vertice_inicial] = 0

    # Question: Why do we iterate over the vertices?
    for _ in range(1, grafo.qtdVertices()):
        for u, v in grafo.arestas:
            peso = grafo.peso(u,v)
            if D[v] > D[u] + peso:
                D[v] = D[u] + peso
                A[v] = u

    for u, v in grafo.arestas:
        if D[v] > D[u] + grafo.peso(u,v):
            return False, None, None

    return True, D, A


if __name__ == '__main__':
    arquivo = 'arquivos\\facebook_santiago.net'
    grafo = GrafoNaoDirigido(arquivo)
    vertice_inicial = 2

    _, D, A = bellman_ford(grafo, vertice_inicial)

    print_ex_4(D, A)