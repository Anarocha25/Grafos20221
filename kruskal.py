import os
import ast
import numpy as np
from grafo import Grafo
from utils import minimum_spanning_tree

def kruskal(grafo):
    A = []
    S = []

    for v in list(grafo.vertices.keys()):
        S.append([v])
    
    arestas_ordenadas = sorted(grafo.pesos.items(), key=lambda x: x[1])
    E_linha = []
    for aresta in arestas_ordenadas:
        E_linha.append(aresta[0])

    for E in E_linha:
        E0 = ast.literal_eval(E)
        E1 = S[E0[0]-1]
        E1.sort()
        E2 = S[E0[1]-1]
        E2.sort()
        if E1 != E2:
            A.append(E0)
            x = []
            x.extend(E1)
            x.extend(E2)
            x = list(set(x))
            x.sort()
            for y in x:
                S[y-1] = x
    somatorio_pesos = 0
    for aresta in A:
        somatorio_pesos += grafo.peso(aresta[0], aresta[1])

    return A, somatorio_pesos
        
if __name__ == '__main__':
    arquivo = os.path.join('arquivos', 'agm_tiny.net')
    nao_dirigido = True
    grafo = Grafo(arquivo, nao_dirigido)
    A, somatorio_pesos = kruskal(grafo)
    minimum_spanning_tree(A, somatorio_pesos)