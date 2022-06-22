import numpy as np
import os
from parse import search

class Grafo():
    vertices = {}
    arestas = []
    pesos = {}

    def __init__(self, arquivo, nao_dirigido=False) -> None:
        self.nao_dirigido = nao_dirigido
        self.ler(arquivo)

    def qtdVertices(self):
        """ Retorna a quantidade de vértices do grafo """
        return len(self.vertices)

    def qtdArestas(self):
        """ Retorna a quantidade de arestas do grafo """
        return len(self.arestas)

    def grau(self, chave_vertice: int):
        """ Retorna o grau do vértice v
            Args:
                chave_vertice int: Contém a chave do vertice
        """
        return len(self.vizinhos(chave_vertice))

    def rotulo(self, chave_vertice: int):
        """ Retorna o rótulo do vértice v
            Args:
                vertice_v int: Contém a chave do vertice
        """
        return self.vertices[chave_vertice]

    def vizinhos(self, chave_vertice):
        """ Retorna os vizinhos do vértice cuja chave é chave_vertice
            Args:
                chave_vertice int: Contém a chave do vertice
        """
        vizinhos = []
        for aresta in self.arestas:
            if aresta[0] == chave_vertice:
                vizinhos.append(aresta[1])
            if self.nao_dirigido:
                if aresta[1] == chave_vertice and aresta[1] not in vizinhos:
                    vizinhos.append(aresta[0])
        return vizinhos

    def haAresta(self, chave_vertice_1: int, chave_vertice_2: int):
        """ Se {chave_vertice_1, chave_vertice_2} ∈ E, retorna verdadeiro; se não existir, retorna falso

            Args:
                chave_vertice_1 int: Contém a chave do vertice 1
                chave_vertice_2 int: Contém a chave do vertice 2
        """
        if self.nao_dirigido:
            return ((chave_vertice_1, chave_vertice_2) in self.arestas) or ((chave_vertice_2, chave_vertice_1) in self.arestas)
        else:
            return (chave_vertice_1, chave_vertice_2) in self.arestas

    def peso(self, chave_vertice_1, chave_vertice_2):
        """ Se {chave_vertice_1, chave_vertice_2} ∈ E, retorna o peso da aresta {chave_vertice_1, chave_vertice_2}; 
            se não existir, retorna um valor infinito positivo

            Args:
                chave_vertice_1 int: Contém a chave do vertice 1
                chave_vertice_2 int: Contém a chave do vertice 2
        """
        if self.nao_dirigido:
            return self.pesos.get(
                str((chave_vertice_1, chave_vertice_2)),
                self.pesos.get(
                    str((chave_vertice_2, chave_vertice_1)),
                    np.inf
                )
            )
        else:
            return self.pesos.get(
                str((chave_vertice_1, chave_vertice_2)),
                np.inf
            )

    def ler(self, arquivo):
        """ Carrega um grafo a partir de um arquivo .net definido como:
                *vertices n
                1 rotulo_de_1
                2 rotulo_de_2
                ...
                n label_de_n
                *edges
                a b valor_do_peso
                a c valor_do_peso
                ...

            Args:
                arquivo (str): Nome do arquivo contendo o diretório
        """
        with open(arquivo, "r") as file:
            vertices, arestas = file.read().split('*edges')
            vertices = vertices.split('\n')[1:-1]
            
            for ind, vertice in enumerate(vertices):
                numero = search("{:d}", vertice)[0]
                nome = vertice.replace(str(numero), '')
                nome = nome.strip().replace('"', '')
                self.vertices[numero] =  nome
            
            arestas = arestas.split('\n')[1:-1]
            for ind in range(len(arestas)):
                aux = arestas[ind].split()
                aresta = (int(aux[0]), int(aux[1]))
                self.arestas.append(aresta)
                self.pesos[str(aresta)] = float(aux[-1])
        
if __name__ == '__main__':
    arquivo = os.path.join('arquivos', 'dirigido_simpsons_amizades1.net')
    nao_dirigido = False
    grafo = Grafo(arquivo, nao_dirigido)

    assert grafo.qtdVertices() == 12
    assert grafo.qtdArestas() == 52
    assert grafo.grau(1) == 4
    assert grafo.rotulo(1) == "Homer Jay Simpson"
    assert grafo.vizinhos(1) == [2, 3, 4, 5]
    assert grafo.haAresta(1, 2) is True
    assert grafo.haAresta(2, 1) is True
    assert grafo.haAresta(1, 6) is False
    assert grafo.peso(1, 24) == np.inf
    assert grafo.peso(1, 5) == 1.0
    assert grafo.peso(2, 1) == 1.0