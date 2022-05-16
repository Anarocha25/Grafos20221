import numpy as np

def print_ex_4(D, A):
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
