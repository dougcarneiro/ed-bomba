from data_struct.node import Node
from data_struct.data_type import DataType
from data_struct.generic_data_struct import GenericDataStruct
from exceptions import PilhaException


class Pilha(GenericDataStruct):
    """
    Classe que implementa a estrutura de dados "Pilha" utilizando a técnica
    simplesmente encadeada.
    """

    def __init__(self):
        super().__init__()
        self.data_type = DataType.PILHA # Tipo da estrutura: pilha, lista, etc

  
    def top(self):
        """
        Método que devolve o elemento localizado no topo, sem desempilhá-lo
        """
        validation = self.validations()
        if not validation:
            return self.head
        else:
            raise PilhaException(validation)
    

    def stack_up(self, data: str):
        """ 
        Método que adiciona um novo elemento ao topo da pilha
        """
        new = Node(data)
        new.next = self.head
        self.head = new
        self.size += 1


    def unstack(self) -> str:
        """
        Método que remove um elemento do topo da pilha e devolve 
        a carga correspondente a esse elemento removido.
        """
        
        validation = self.validations()
        if not validation:
            node = self.head
            self.head = self.head.next
            self.size -= 1
            return node.data
        else:
            raise PilhaException(validation)
