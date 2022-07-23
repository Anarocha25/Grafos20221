from grafo import Grafo
import numpy as np
import os
import itertools

def subconjuntos_possiveis(lista_vertices):
    combinations = []
    for r in range(len(lista_vertices)+1):
        for combination in itertools.combinations(lista_vertices, r):
            if len(combination) > 0:
                combinations.append(list(combination))
    return combinations

def conjuntos_ind_max(vertices_G, arestas_G):
    sub_S = subconjuntos_possiveis(vertices_G)
    R = []
    for X in reversed(sub_S):
        c = True
        for v in X:
            for u in X:
                if (u,v) in arestas_G:
                    c = False
        if c:
            R.append(X)
    return R

def encontrar_conj_i(subconj_S, conj_S, conj_I):
    i = subconj_S.copy()
    for val_I in conj_I:
        i.remove(val_I)
    for row_conj_S in range(len(conj_S)):
        if conj_S[row_conj_S] == i:
            ind_i = row_conj_S
            break
    return ind_i

def coloracao(G):
    rows = 2**G.qtdVertices()
    cols = G.qtdVertices()
    tabela_aux = np.zeros((rows, cols))
    val_repete = 1
    for col in range(cols-1, -1, -1):
        val = np.tile(np.repeat([0, 1], val_repete), int(rows/(2*val_repete)))
        tabela_aux[:, col] = val
        val_repete *= 2

    vertices = list(G.vertices.keys())
    conjunto_S = []
    for row in range(rows):
        ind = np.where(tabela_aux[row, :] == 1)[0]
        if len(ind) > 0:
            v_sele = []
            for i in ind:
                v_sele.append(vertices[i])
            conjunto_S.append(v_sele)
        else:
            conjunto_S.append([])

    X = np.zeros(rows)
    for ind, S in enumerate(conjunto_S):
        if len(S) == 1:
            X[ind] = 1
        elif len(S) > 1:
            X[ind] = np.inf

            # Grafo G-linha
            arestas_G_linha = []
            for combination in itertools.combinations(S, 2):
                if combination in G.arestas:
                    arestas_G_linha.append(combination)
            vertices_G_linha = S

            I_G_linha = conjuntos_ind_max(vertices_G_linha, arestas_G_linha)
            for I in I_G_linha:
                ind_i = encontrar_conj_i(S, conjunto_S, I)
                if X[ind_i] + 1 < X[ind]:
                    X[ind] = X[ind_i] + 1
    return int(np.max(X))

def obter_cor_vertice(G, min_cor):
    cor_vertices = np.full(G.qtdVertices(), np.inf)
    cores = np.arange(0, min_cor)
    for vertice in list(G.vertices.keys()):
        if cor_vertices[vertice - 1] == np.inf:
            vizinhos = G.vizinhos(vertice)
            cores_vizinhos = []
            for vizinho in vizinhos:
                if cor_vertices[vizinho -1] != np.inf:
                    cores_vizinhos.append(cor_vertices[vizinho -1])
            if len(cores_vizinhos) > 0:
                for cor in cores:
                    if cor not in cores_vizinhos:
                        cor_vertice = cor
                        break
                cor_vertices[vertice - 1] = cor_vertice
            else:
                cor_vertices[vertice - 1] = cores[0]

    return dict(zip(list(G.vertices.keys()), cor_vertices))

if __name__ == '__main__':

    arquivo = os.path.join('arquivos', 'nao_dirigido.net')
    grafo = Grafo(arquivo, nao_dirigido=True)
    qtd_cores = coloracao(grafo)
    print("Quantidade mínima de cores: ", qtd_cores)

    cor_cada_vertice = obter_cor_vertice(grafo, qtd_cores)
    print("\nCor associada a cada vértice: ", cor_cada_vertice)
