from data_struct.node import Node
from exceptions import ListaException
from data_struct.data_type import DataType
from data_struct.generic_data_struct import GenericDataStruct


class Lista(GenericDataStruct):
    '''
    Esta classe implementa uma estrutura Lista Simplesmente Encadeada Circular
    '''
    def __init__(self):
        super().__init__()
        self.data_type = DataType.LISTA

    def edit_node_data(self, position, data):
        cursor = self.get_node(position)
        cursor.data = data
        

    def insert(self, position, data):
        # CONDICAO 1: insercao se a lista estiver vazia
        new_node = Node(data)
        is_empty, empty_validation = self.is_empty()
        if is_empty:
            self.head = new_node
            self.head.next = self.head
            self.size += 1
            return
        
        # CONDICAO 2: insercao na primeira posicao em uma lista nao vazia
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return

        # CONDICAO 3: insercao apos a primeira posicao em lista nao vazia
        ok_position, msg_excpt =  self.check_position(position, plus=1)
        if not ok_position:
            raise ListaException(msg_excpt)
            
        cursor = self.get_node(position, minus=1)
        new_node.next = cursor.next
        cursor.next = new_node
        self.size += 1

    def remove(self, position):
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
        return removed
    
    def move_around(self, times, start_node=None):
        count = 1
        node = start_node if start_node else self.head
        while count <= times:
            node = node.next
            count += 1
        return node

