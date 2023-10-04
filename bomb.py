from random import randint

from data_struct.lista_encadeada_circular import Lista
from data_struct.pilha_encadeada import Pilha


class BombSimulator:
    def __init__(self,
                 participants:list[str],
                 pointer:str=None,
                 round:int=1,
                 winners:int=1,
                 time_min:int=4,
                 time_max:int=15,
                 removed_pile:list[str]=None):
        self.__round = round
        self.__winners = winners
        self.__pointer = pointer
        self.__time_min = time_min
        self.__time_max = time_max
        self.__participants = participants
        self.__removed_pile = removed_pile
        self.prep_participants()
        self.prep_removed_file()
    
    def prep_participants(self):
        linked_list = Lista()
        for i in range(len(self.__participants)):
            linked_list.insert(i+1, self.__participants[i])
        self.participants = linked_list
            
    def prep_removed_file(self):
        removed_pile = Pilha()
        if self.__removed_pile:
            for elem in reversed(self.__removed_pile):
                removed_pile.stack_up(elem)
            self.removed_pile = removed_pile
        self.removed_pile = removed_pile
            
    
    @property
    def round(self):
        return self.__round
    
    @round.setter
    def round(self, new_round):
        self.__round = new_round
        
    @property
    def winners(self):
        return self.__winners
    
    @winners.setter
    def winners(self, new_winners):
        self.__winners = new_winners
        
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
    
    @removed_pile.setter
    def removed_pile(self, new_removed_pile):
        self.__removed_pile = new_removed_pile
        
    @property
    def time_min(self):
        return self.__time_min
    
    @time_min.setter
    def time_min(self, new_time_min):
        self.__time_min = new_time_min
        
    @property
    def time_max(self):
        return self.__time_max
    
    @time_max.setter
    def time_max(self, new_time_max):
        self.__time_max = new_time_max
        
        
    def summary(self, path, k=None):
        participants = self.participants.__str__().replace(
            self.participants.data_type.value.title(), 'Participantes')
        summary = (f'\n{participants}\nRound: {self.round}\n'
               f'Pointer: {self.pointer}\n'
               f'Caminho da bomba: {path}\n'
               f'Removido: {self.__removed_pile.top()}  k: {k}\n')
        return summary


    def move_around(self, times, start_node):
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
        if not self.pointer:
            self.pointer = self.participants.get_random_node(min=self.time_min,
                                                             max=self.time_max)
        k = randint(self.time_min, self.time_max)
        node_data, next_data, path = self.move_around(
            start_node=self.pointer if self.pointer else None,
            times=k)
        node_position = self.participants.search_by_value(node_data)
        self.removed_pile.stack_up(node_data)
        summary = self.summary(k=k, path=path)
        self.pointer = next_data
        self.participants.remove(node_position)
        if not self.participants.size == self.winners:
            self.round += 1
        return summary
