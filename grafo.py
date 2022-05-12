import numpy as np
from parse import search

class GrafoNaoDirigido():
    def __init__(self, arquivo) -> None:
        self.ler(arquivo)

    def qtdVertices(self):
        """ Retorna a quantidade de vértices do grafo """
        return len(self.vertices)

    def qtdArestas(self):
        """ Retorna a quantidade de arestas do grafo """
        return len(self.arestas)

    def grau(self, vertice_v):
        """ Retorna o grau do vértice v
            Args:
                vertice_v (tuple): Contém o identificador e o rótulo do vertice
        """
        return len(self.vizinhos(vertice_v))

    def rotulo(self, vertice_v):
        """ Retorna o rótulo do vértice v
            Args:
                vertice_v (tuple): Contém o identificador e o rótulo do vertice
        """
        return vertice_v[1]

    def vizinhos(self, vertice_v):
        """ Retorna os vizinhos do vértice v
            Args:
                vertice_v (tuple): Contém o identificador e o rótulo do vertice
        """
        vizinhos = []
        for aresta in self.arestas:
            if aresta[0] == self.grau(vertice_v):
                vizinhos.append(aresta[1])
            elif aresta[1] == self.grau(vertice_v):
                vizinhos.append(aresta[0])
        return vizinhos

    def haAresta(self, vertice1, vertice2):
        """ Se {vertice1, vertice2} ∈ E, retorna verdadeiro; se não existir, retorna falso

            Args:
                vertice1 (tuple): Contém o identificador e o rótulo do vertice 1
                vertice2 (tuple): Contém o identificador e o rótulo do vertice 2
        """
        return (self.grau(vertice1), self.grau(vertice2)) in self.arestas

    def peso(self, vertice1, vertice2):
        """ Se {vertice1, vertice2} ∈ E, retorna o peso da aresta {vertice1, vertice2}; 
            se não existir, retorna um valor infinito positivo

            Args:
                vertice1 (tuple): Contém o identificador e o rótulo do vertice 1
                vertice2 (tuple): Contém o identificador e o rótulo do vertice 2
        """
        if self.haAresta(vertice1, vertice2):
            ind = self.arestas.index((self.grau(vertice1), self.grau(vertice2)))
            return self.pesos[ind]
        else:
            return np.inf

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
            arestas = arestas.split('\n')[1:-1]
            self.vertices = []
            self.arestas = []
            self.pesos = []
            for ind, vertice in enumerate(vertices):
                numero = search("{:d}", vertice)[0]
                nome = vertice.replace(str(numero), '')
                nome = nome.strip().replace('"', '')
                self.vertices.append((numero, nome))

                aux = arestas[ind].split()
                self.arestas.append((int(aux[0]), int(aux[1])))
                self.pesos.append(float(aux[-1]))
        
if __name__ == '__main__':
    arquivo = 'facebook_santiago.net'
    grafo_face = GrafoNaoDirigido(arquivo)