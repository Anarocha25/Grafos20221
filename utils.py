import numpy as np

def print_ex_2(D: np.array, vertice_s: int):
    print(0, ': ', vertice_s)
    matriz_aux = np.empty((len(D), 2))
    matriz_aux[:, 0] = np.arange(1, len(D)+1)
    matriz_aux[:, 1] = D
    matriz_aux = matriz_aux[matriz_aux[:, 1].argsort()]
    for ind, val in enumerate(np.unique(matriz_aux[:, 1])):
        if val != 0:
            indices = np.where(matriz_aux[:, 1] == ind)[0]
            print(ind, ": ", matriz_aux[indices,0])


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

def print_ex_5(D: np.array):
    for ind in range(len(D)):
        distancia = D[ind, :].tolist()
        aux = [str(ind+1), distancia]
        print(aux[0], ': ', aux[1])