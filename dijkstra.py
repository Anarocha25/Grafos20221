import numpy as np
import os
from grafo import GrafoNaoDirigido
from utils import print_ex_4

def dijkstra(grafo: GrafoNaoDirigido, vertice_inicial: int):
    D = {vertice: np.inf for vertice in grafo.vertices}
    A = {vertice: None for vertice in grafo.vertices}
    C = {vertice: False for vertice in grafo.vertices}
    D[vertice_inicial] = 0

    while not all(C.values()):
        Dn = {u: D[u] for u in D if C[u] is False}
        u = min(Dn, key=Dn.get)
        C[u] = True
        for v in [i for i in grafo.vizinhos(u) if C[i] is False]:
            peso = grafo.peso(u, v)
            if D[v] > D[u] + peso:
                D[v] = D[u] + peso
                A[v] = u

    return D, A


if __name__ == '__main__':
    vertice_inicial = input("Vértice inicial (int): ")
    try:
        vertice_inicial = int(vertice_inicial)
    except ValueError:
        raise ValueError("Vértice inicial tem que ser um número")

    arquivo = os.path.join('arquivos', 'facebook_santiago.net')
    grafo = GrafoNaoDirigido(arquivo)

    D, A = dijkstra(grafo, vertice_inicial)

    print_ex_4(D, A)