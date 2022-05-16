import numpy as np
from grafo import GrafoNaoDirigido

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
    arquivo = 'facebook_santiago.net'
    grafo = GrafoNaoDirigido(arquivo)
    vertice_inicial = 2

    _, D, A = bellman_ford(grafo, vertice_inicial)

    for vertice, distancia in list(D.items()):
        if distancia == np.inf:
            continue

        vertice_anterior = A[vertice]
        caminho = []
        while vertice_anterior is not None:
            caminho.append(str(vertice_anterior))
            vertice_anterior = A[vertice_anterior]

        caminho = [str(vertice)] + caminho
        print(f"{vertice}: {', '.join(reversed(caminho))}; d={distancia}")