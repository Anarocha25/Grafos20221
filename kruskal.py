import os
import ast
import numpy as np
from grafo import Grafo

def kruskal(grafo):
    A = []
    S = np.empty(len(grafo.vertices), dtype=object)
    
    for v in grafo.vertices.keys():
        S[v-1] = v
    
    E_linha = list(dict(sorted(grafo.pesos.items(), key=lambda item: item[1])).keys())

    for E in E_linha:
        E0 = ast.literal_eval(E)
        E1 = S[E0[0]-1]
        E2 = S[E0[1]-1]
        if E1 != E2:
            A.append(E0)
            for y in E0:
                S[y-1] = E0
    somatorio_pesos = 0
    for aresta in A:
        somatorio_pesos += grafo.peso(aresta[0], aresta[1])

    return A, somatorio_pesos
        
if __name__ == '__main__':
    arquivo = os.path.join('arquivos', 'agm_tiny.net')
    nao_dirigido = True
    grafo = Grafo(arquivo, nao_dirigido)
    A, somatorio_pesos = kruskal(grafo)
    print("teste")