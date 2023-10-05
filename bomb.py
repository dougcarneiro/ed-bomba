from random import randint

from data_struct.lista_encadeada_circular import Lista
from data_struct.pilha_encadeada import Pilha


class BombSimulator:
    '''
    Classe que implementa um círculo da bomba
    '''
    def __init__(self,
                 participants:list[str],
                 winners:int=1):
        self.__round = 1
        self.__winners = winners
        self.__pointer = None
        self.__time_min = 4
        self.__time_max = 15
        self.__participants = participants
        self.__removed_pile = Pilha()
        self.prep_participants()
    
    def prep_participants(self):
        '''
        Método para ler uma lista de participantes e os organiza dentro da 
        estrutura de dados necessária para o círculo da bomba
        '''
        linked_list = Lista()
        for i in range(len(self.__participants)):
            linked_list.insert(i+1, self.__participants[i])
        self.participants = linked_list

    
    @property
    def round(self):
        return self.__round
    
    @round.setter
    def round(self, new_round):
        self.__round = new_round
        
    @property
    def winners(self):
        return self.__winners
        
    @property
    def pointer(self):
        return self.__pointer
    
    @pointer.setter
    def pointer(self, new_pointer):
        self.__pointer = new_pointer

    @property
    def participants(self):
        return self.__participants
    
    @participants.setter
    def participants(self, new_participants):
        self.__participants = new_participants
    
    @property
    def removed_pile(self):
        return self.__removed_pile
    
    @property
    def time_min(self):
        return self.__time_min
    
    @property
    def time_max(self):
        return self.__time_max


    def summary(self, path, k):
        '''
        Método que formata e retorna uma string com as informações da rodada
        '''
        participants = self.participants.__str__().replace(
            self.participants.data_type.value.title(), 'Participantes')
        summary = (f'\n{participants}\nRound: {self.round}\n'
               f'Pointer: {self.pointer}\n'
               f'Caminho da bomba: {path}\n'
               f'Removido: {self.__removed_pile.top()}  k: {k}\n')
        return summary


    def move_around(self, times, start_node):
        '''
        Método que circula a bomba entre os participantes, partindo de um
        ponteiro, e retorna o valor do nó em que a bomba parou
        '''
        node = start_node
        count = 1
        str = '['
        while count <= times:
            node = self.participants.get_next(node)
            str += f' {node} >'
            count += 1
        path = str[:-2] + ' ]'
        return node, self.participants.get_next(node), path


    def go(self):
        '''
        Método inicia a rodada e faz a bomba circular uma vez entre os 
        participantes
        '''
        if not self.pointer:
            self.pointer = self.participants.get_random_node()
        k = randint(self.time_min, self.time_max)
        node_data, next_data, path = self.move_around(
            start_node=self.pointer,times=k)
        node_position = self.participants.search_by_value(node_data)
        self.removed_pile.stack_up(node_data)
        summary = self.summary(k=k, path=path)
        self.pointer = next_data
        self.participants.remove(node_position)
        # Verificamos se o número restante de participantes está igual ao de vencedores
        # antes de incrementar a rodada/round
        if not (self.participants.size == self.winners):
            self.round += 1
        return summary
