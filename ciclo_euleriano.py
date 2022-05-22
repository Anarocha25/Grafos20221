import numpy as np
from grafo import GrafoNaoDirigido
from utils import print_ex_4

def buscar_subciclo_euleriano_aux(grafo: GrafoNaoDirigido,v, C):
    ciclo = [v]
    t = v
    r = True
    while True:
        vizinhos = grafo.vizinhos(v)
        for vizinho in vizinhos:
            try:
                if C[str((vizinho, v))] == True:
                    return False, None, None
            except KeyError:
                pass
            else:
                for aresta in grafo.arestas:
                    if C[str(aresta)] == False:
                        aresta_escolhida = aresta
                        break
                C[str(aresta_escolhida)] = True
                v = aresta_escolhida[1]
                ciclo.append(v)    
        if t == v:
            break
    return r, C, ciclo
    
def buscar_subciclo_euleriano(grafo: GrafoNaoDirigido,v, C):
    r, C, ciclo = buscar_subciclo_euleriano_aux(grafo, v, C)
    if r == False:
        return False, None
    ciclo_final = ciclo.copy()
    for ind, x in enumerate(ciclo):
        vizinhos = grafo.vizinhos(x)
        for vizinho in vizinhos:
            if C[str((x, vizinho))] == False:
                r, C, ciclo_linha = buscar_subciclo_euleriano_aux(grafo, x, C)
                if r == False:
                    return False, None
        ciclo_final[ind] = ciclo_linha
    return True, C, ciclo_final

def hierholzer(grafo: GrafoNaoDirigido):
    C = dict([(str(aresta), False) for aresta in grafo.arestas])
    for vertice in grafo.vertices:
        if grafo.grau(vertice) > 0:
            v = vertice
            break

    r, C, ciclo = buscar_subciclo_euleriano(grafo,v, C)
    if r == False:
        return 0
    else:
        if False in C.values():
            return 0
        else:
            return 1, ciclo

if __name__ == '__main__':
    arquivo = 'facebook_santiago.net'
    grafo_face = GrafoNaoDirigido(arquivo)
    teste = hierholzer(grafo_face)
    print(teste)

