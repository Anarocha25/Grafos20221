import os
import numpy as np
from grafo import Grafo
import copy


def comp_forte_conexos(grafo: Grafo):
    F = {vertice: np.inf for vertice in grafo.vertices}
    next(DFS(grafo, F))

    grafo_t = copy.deepcopy(grafo)
    grafo_t.arestas = [(v, u) for u, v in grafo.arestas]

    # Yields árvores
    yield from DFS(grafo_t, F)

def DFS(grafo: Grafo, F):
    C = {vertice: False for vertice in grafo.vertices}
    T = {vertice: np.inf for vertice in grafo.vertices}

    # Declarado como uma lista para declarar a variável como um ponteiro
    tempo = [0]

    for u in sorted(grafo.vertices, key=lambda v: F[v], reverse=True):
        # Criar uma árvore nova para cada iteração
        A = {vertice: None for vertice in grafo.vertices}
        if C[u] is False:
            DFS_visit(grafo, u, C, T, A, F, tempo)
            yield A

def DFS_visit(grafo: Grafo, v, C, T, A, F, tempo):
    C[v] = True
    tempo[0] += 1
    T[v] = tempo[0]

    for u in grafo.vizinhos(v):
        if C[u] is False:
            A[u] = v
            DFS_visit(grafo, u, C, T, A, F, tempo)

    tempo[0] += 1
    F[v] = tempo[0]

if __name__ == '__main__':
    arquivo = os.path.join('arquivos', 'componentes.net')
    grafo = Grafo(arquivo, nao_dirigido=False)

    # Achar componentes fortemente conexos
    # A se refere a uma árvore.
    componentes = []
    for A in comp_forte_conexos(grafo):
        vertices_com_antecessores = [(k, v) for k, v in A.items() if v is not None]
        if vertices_com_antecessores:
            flat_list = {item for sublist in vertices_com_antecessores for item in sublist}
            componentes.append(flat_list)

    # Adicionar vértices isolados. Esses não possuem nenhum sucessor.
    vertices_in_componentes = {item for sublist in componentes for item in sublist}
    for v in grafo.vertices:
        if v not in vertices_in_componentes:
            componentes.append({v})

    for componente in componentes:
        print(", ".join([str(c) for c in componente]))
