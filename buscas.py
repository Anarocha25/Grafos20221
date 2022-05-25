import numpy as np
import os
from grafo import GrafoNaoDirigido
from utils import print_ex_2

def busca_largura(grafo: GrafoNaoDirigido, vertice_s: int):
    qtd_vertices = grafo.qtdVertices()
    C = np.full(qtd_vertices, False)
    D = np.full(qtd_vertices, np.inf)
    A = np.full(qtd_vertices, None)

    C[vertice_s - 1] = True
    D[vertice_s - 1] = 0

    Q = []
    Q.append(vertice_s)

    while len(Q) > 0:
        u = Q[0]
        Q.pop(0)

        for vizinho in grafo.vizinhos(u):
            if C[vizinho - 1] == False:
                C[vizinho - 1] = True
                D[vizinho - 1] = D[u - 1] + 1
                A[vizinho - 1] = u
                Q.append(vizinho)

    return D, A

if __name__ == '__main__':
    vertice_inicial = input("Vértice inicial (int): ")
    try:
        vertice_inicial = int(vertice_inicial)
    except ValueError:
        raise ValueError("Vértice inicial tem que ser um número")

    arquivo = os.path.join('arquivos', 'buscas.net')
    grafo1 = GrafoNaoDirigido(arquivo)
    vertice_inicial = 7
    D, A = busca_largura(grafo1, vertice_inicial)

    print_ex_2(D, vertice_inicial)