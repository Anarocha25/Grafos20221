import numpy as np
import os
from utils import print_ex_5
from grafo import GrafoNaoDirigido

def floyd_warshall(grafo: GrafoNaoDirigido):
    D = np.empty((grafo.qtdVertices(), grafo.qtdVertices()))
    D.fill(np.inf)
    np.fill_diagonal(D, 0)
    for vertice in grafo.vertices:
        vizinhos = grafo.vizinhos(vertice) 
        for vizinho in vizinhos:
            peso = grafo.peso(vertice, vizinho)
            D[vertice-1, vizinho-1] = peso
    
    for vertice_k in grafo.vertices:
        for vertice_u in grafo.vertices:
            for vertice_v in grafo.vertices:
                D[vertice_u-1, vertice_v-1] = min(D[vertice_u-1, vertice_v-1], D[vertice_u-1, vertice_k-1] + D[vertice_k-1, vertice_v-1])
    return D

if __name__ == '__main__':
    arquivo = os.path.join('arquivos', 'floyd_warshall_small.net')
    grafo_face = GrafoNaoDirigido(arquivo)

    resposta = floyd_warshall(grafo_face)

    print_ex_5(resposta)

    # gabarito =  np.empty((6,6))
    # gabarito.fill(np.inf)
    # np.fill_diagonal(gabarito, 0)

    # gabarito[1,0] = 4
    # gabarito[2,0] = 3

    # gabarito[0,1] = 1
    # gabarito[2,1] = 4

    # gabarito[0,2] = 2
    # gabarito[1,2] = 1

    # gabarito[0,3] = 0
    # gabarito[1,3] = -1
    # gabarito[2,3] = 2
    # gabarito[4,3] = -3
    # gabarito[5,3] = 0

    # gabarito[0,4] = 3
    # gabarito[1,4] = 2
    # gabarito[2,4] = 6
    # gabarito[3,4] = 5
    # gabarito[5,4] = 3

    # gabarito[0,5] = 2
    # gabarito[1,5] = 1
    # gabarito[2,5] = 4
    # gabarito[3,5] = 2
    # gabarito[4,5] = -1
