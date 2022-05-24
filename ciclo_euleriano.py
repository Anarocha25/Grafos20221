import numpy as np
import os
from grafo import GrafoNaoDirigido
import random
import os
from utils import print_ex_3

# Algoritmo baseado na aula:
# https://www.youtube.com/watch?v=G1diwiNcAk8&ab_channel=Prof.AlexandreLevada
def ciclo_euleriano(grafo: GrafoNaoDirigido):
    for vertice in grafo.vertices:
        if grafo.grau(vertice)%2 != 0:
            return []
    
    C = dict([(str(aresta), False) for aresta in grafo.arestas])
    for vertice in grafo.vertices:
        if grafo.grau(vertice) > 0:
            v = vertice
            break
    S = [v]
    T = []
    while len(S) > 0:
        u = S[-1]
        vizinhos = grafo.vizinhos(u)

        vizinho_u = vizinhos[random.randint(0, len(vizinhos))-1]

        try:
            if C[str((vizinho_u, u))] == False:
                S.append(vizinho_u)
                C[str((vizinho_u, u))] = True

        except KeyError:
            if C[str((u, vizinho_u))] == False:
                S.append(vizinho_u)
                C[str((u, vizinho_u))] = True

        arestas_verificadas = np.empty(len(vizinhos), dtype=bool)
        for ind, vizinho in enumerate(vizinhos):
            try:
                arestas_verificadas[ind] = C[str((vizinho, u))]
            except KeyError:
                arestas_verificadas[ind] = C[str((u, vizinho))]

        if u == S[-1] and arestas_verificadas.all():
            T.append(S[-1])
            S.pop(-1)
    return T
    
if __name__ == '__main__':
    arquivo = os.path.join('arquivos', 'ContemCicloEuleriano.net')
    grafo = GrafoNaoDirigido(arquivo)
    ciclo = ciclo_euleriano(grafo)

    print_ex_3(ciclo)