from data_struct.node import Node
from data_struct.data_type import DataType
from data_struct.generic_data_struct import GenericDataStruct
from exceptions import PilhaException


class Pilha(GenericDataStruct):
    """
    Classe que implementa a estrutura de dados "Pilha" utilizando a técnica
    simplesmente encadeada.

     Attributes:
        head (Node): apontador para o nó topo da pilha
        tamanho (int): quantidade de elementos existentes na pilha
    """

    def __init__(self):
        super().__init__()
        self.data_type = DataType.PILHA

  
    def top(self):
        """ Método que devolve o elemento localizado no topo, sem desempilhá-lo
    
        Returns:
            any: o conteúdo referente ao elemento do topo

        Raises:
            PilhaException: Exceção lançada quando se tenta consultar o topo de uma
                   uma pilha vazia
                    
        Examples:
            p = Pilha()
            ...   # considere que temos internamente a lista [10,20,30,40]
            dado = p.topo()
            print(dado) # exibe 40
        """
        validation = self.validations()
        if not validation:
            return self.head
        else:
            raise PilhaException(validation)
    

    def stack_up(self, data):
        """ Método que adiciona um novo elemento ao topo da pilha

        Argumentoss:
            carga(any): o conteúdo a ser inserido no topo da pilha.

        Examples:
            p = Pilha()
            # considere a pilha  topo->[10,20,30,40]
            p.empilha(50)
            print(p)  # exibe [10,20,30,40,50]
        """
        new = Node(data)
        new.next = self.head
        self.head = new
        self.size += 1


    def unstack(self):
        """ Método que remove um elemento do topo da pilha e devolve 
            a carga correspondente a esse elemento removido.
    
        Returns:
            any: a carga removida do topo da pilha

        Raises:
            PilhaException: Exceção lançada quando se tenta remover de uma pilha vazia
                    
        Examples:
            p = Pilha()
            # considere que temos internamente a pilha [10,20,30,40]<-topo
            dado = p.desemplha()
            print(p) # exibe [10,20,30]
            print(dado) # exibe 40
        """
        
        validation = self.validations()
        if not validation:
            node = self.head
            self.head = self.head.next
            self.size -= 1
            return node
        else:
            raise PilhaException(validation)
