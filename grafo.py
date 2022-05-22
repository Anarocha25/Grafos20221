import numpy as np
from parse import search

class GrafoNaoDirigido():
    vertices = {}
    arestas = []
    pesos = {}

    def __init__(self, arquivo) -> None:
        self.ler(arquivo)

    def qtdVertices(self):
        """ Retorna a quantidade de vértices do grafo """
        return len(self.vertices)

    def qtdArestas(self):
        """ Retorna a quantidade de arestas do grafo """
        return len(self.arestas)

    def grau(self, vertice_key: int):
        """ Retorna o grau do vértice v
            Args:
                vertice_key int: Contém a chave do vertice
        """
        return len(self.vizinhos(vertice_key))

    def rotulo(self, vertice_key: int):
        """ Retorna o rótulo do vértice v
            Args:
                vertice_v int: Contém a chave do vertice
        """
        return self.vertices[vertice_key]

    def vizinhos(self, vertice_key):
        """ Retorna os vizinhos do vértice cuja chave é vertice_key
            Args:
                vertice_key int: Contém a chave do vertice
        """
        vizinhos = []
        for aresta in self.arestas:
            if aresta[0] == vertice_key:
                vizinhos.append(aresta[1])
            elif aresta[1] == vertice_key:
                vizinhos.append(aresta[0])
        return vizinhos

    def haAresta(self, vertice_key_1: int, vertice_key_2: int):
        """ Se {vertice_key_1, vertice_key_2} ∈ E, retorna verdadeiro; se não existir, retorna falso

            Args:
                vertice_key_1 int: Contém a chave do vertice 1
                vertice_key_2 int: Contém a chave do vertice 2
        """
        return (vertice_key_1, vertice_key_2) in self.arestas

    def peso(self, vertice_key_1, vertice_key_2):
        """ Se {vertice_key_1, vertice_key_2} ∈ E, retorna o peso da aresta {vertice_key_1, vertice_key_2}; 
            se não existir, retorna um valor infinito positivo

            Args:
                vertice_key_1 int: Contém a chave do vertice 1
                vertice_key_2 int: Contém a chave do vertice 2
        """
        return self.pesos.get(
            str((vertice_key_1, vertice_key_2)),
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
    arquivo = 'arquivos\\facebook_santiago.net'
    grafo_face = GrafoNaoDirigido(arquivo)

    assert grafo_face.qtdVertices() == 688
    assert grafo_face.qtdArestas() == 8725
    assert grafo_face.grau(1) == 58
    assert grafo_face.rotulo(1) == "João Luiz Ferreira Júnior"
    assert grafo_face.vizinhos(1) == [
        135, 269, 653, 565, 221, 657, 367, 315, 143, 451, 147, 662, 227, 150, 412, 322,
        349, 573, 317, 328, 577, 534, 283, 237, 586, 244, 336, 506, 542, 589, 250, 257,
        294, 591, 40, 342, 239, 168, 169, 387, 299, 206, 433, 554, 207, 649, 562, 302,
        521, 260, 131, 256, 241, 512, 53, 98, 211, 12
    ]
    assert grafo_face.haAresta(1, 135) is True
    assert grafo_face.haAresta(1, 136) is False
    assert grafo_face.peso(1, 2) == np.inf
    assert grafo_face.peso(1, 12) == 1.0