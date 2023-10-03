from random import randint

from data_struct.lista_encadeada_circular import Lista
from data_struct.pilha_encadeada import Pilha


class BombSimulator:
    def __init__(self,
                 participants,
                 pointer=None,
                 round=1,
                 winners=1,
                 time_min=4,
                 time_max=15,
                 removed_pile=None):
        self.__round = round
        self.__winners = winners
        self.__pointer = pointer
        self.__time_min = time_min
        self.__time_max = time_max
        self.__participants = participants
        self.__removed_pile = removed_pile if removed_pile else Pilha()
        self.prep_participants()
    
    def prep_participants(self):
        if type(self.participants) is Lista:
            return
        elif type(self.participants) is list:
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
        
        
    def summary(self, k=None):
        participants = self.participants.__str__().replace(
            self.participants.data_type.value.title(), 'Participantes')
        summary = (f'\n{participants}\nRound: {self.round}\n'
               f'Pointer: {self.pointer}\n'
               f'Removido: {self.__removed_pile.top()}  k: {k}\n')
        return summary


    def move_around(self, times, start_node=None):
        count = 1
        node = start_node if start_node else self.participants.head
        while count <= times:
            node = node.next
            count += 1
        return node

        
    def go(self):
        if not self.pointer:
            self.pointer = self.participants.get_node(
                randint(1, self.participants.size))
        k = randint(self.time_min, self.time_max)
        node = self.move_around(
            start_node=self.pointer if self.pointer else None,
            times=k)
        node_position = self.participants.search_by_value(node.data)
        self.removed_pile.stack_up(node)
        summary = self.summary(k)
        self.pointer = node.next
        self.participants.remove(node_position)
        if not self.participants.size == self.winners:
            self.round += 1
        return summary
