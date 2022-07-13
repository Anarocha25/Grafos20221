import numpy as np
import os
from grafo import Grafo

def edmonds_karp(G, G_res, vertice_s, vertice_t):
    C = np.full(G.qtdVertices(), False)
    C[vertice_s - 1] = True
    A = np.full(G.qtdVertices(), None)

    Q = []
    Q.append(vertice_s)
    p = []
    while len(Q) > 0:
        u = Q[0]
        Q.pop(0)
        
        for vizinho in G.vizinhos(u):
            if C[vizinho - 1] == False and G_res.peso(u, vizinho) > 0:
                C[vizinho - 1] = True
                A[vizinho - 1] = u
                if vizinho == vertice_t:
                    p.append(vertice_t)
                    w = vertice_t
                    while w != vertice_s:
                        w = A[w-1]
                        if w not in p:
                            p.append(w)
                    p.reverse()
                    return p
                Q.append(vizinho)
    return None

def obtem_fluxo_maximo(caminho):
    total = 0
    anterior = np.inf
    if caminho is not None:
        for ind in range(len(caminho[:-1])):
            atual = grafo.peso(caminho[ind], caminho[ind+1])
            if atual > anterior:
                total += anterior
            else:
                total += atual
            anterior = atual

        print("Fluxo Máximo: ", total)
    else:
        print("Não possui caminho")

if __name__ == '__main__':

    arquivo = os.path.join('arquivos', 'dirigido1.net')
    grafo = Grafo(arquivo)
    G_res = Grafo(arquivo)
    vertice_s = 1 
    vertice_t = 6

    caminho = edmonds_karp(grafo, G_res, vertice_s, vertice_t)

    obtem_fluxo_maximo(caminho)