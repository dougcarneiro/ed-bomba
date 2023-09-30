class Node:
    '''
    Classe de objetos para um nó dinâmico na memória
    '''
    def __init__(self, data):
        self.__data = data
        self.__next = None
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, new_data):
        self.__data = new_data

    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, new_next):
        self.__next = new_next

    def has_next(self):
        return self.__next != None
    
    def __str__(self):
        return str(self.__data)
