from data_struct.node import Node
from exceptions import ListaException
from data_struct.data_type import DataType
from data_struct.generic_data_struct import GenericDataStruct


class Lista(GenericDataStruct):
    '''
    Esta classe implementa uma estrutura Lista Simplesmente Encadeada Circular
    '''
    def __init__(self):
        super().__init__() # Herdamos os atributos e métodos da super classe
        self.data_type = DataType.LISTA # Tipo da estrutura: pilha, lista, etc

    def edit_node_data(self, position:int, data:str):
        '''
        Método para modificar a carga de um nó a partir de sua posição
        '''
        cursor = self.get_node(position)
        cursor.data = data

    def insert(self, position:int, data:str):
        '''
        Método para inserir um novo elemento na lista
        '''
        # CONDIÇÃO 1: inserção se a lista estiver vazia
        new_node = Node(data)
        is_empty, empty_validation = self.is_empty()
        if is_empty:
            self.head = new_node
            self.head.next = self.head
            self.size += 1
            return
        
        # CONDIÇÃO 2: inserção na primeira posição em uma lista não vazia
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return

        # CONDIÇÃO 3: inserção apos a primeira posição em lista não vazia
        ok_position, msg_excpt =  self.check_position(position, plus=1)
        if not ok_position:
            raise ListaException(msg_excpt)
            
        cursor = self.get_node(position, minus=1)
        new_node.next = cursor.next
        cursor.next = new_node
        self.size += 1

    def remove(self, position:int) -> str:
        '''
        Método para eliminar um nó da lista a partir de sua posição
        '''
        validation = self.validations(position=position)
        if validation:
            raise ListaException(validation)
        cursor = self.get_node(position, minus=1)
        removed = cursor.next
        previous = cursor
        cursor = cursor.next

        if position == 1:
            self.head = cursor
            last_node = self.get_node(position=self.size, minus=1)
            last_node.next = self.head
        else:
            previous.next = cursor.next

        self.size -= 1
        return removed.data
    
