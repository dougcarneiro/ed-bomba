from exceptions import ListaException, PilhaException
from data_struct.data_type import DataType

class GenericDataStruct:
    def __init__(self):
        self.__head = None
        self.__size = 0
        self.__data_type = DataType.UNDEFINED
        
    def __str__(self):
        str = f'{self.__data_type.value.title() if self.__data_type != DataType.UNDEFINED else "Início"}: [ '
        is_empty, empty_excpt = self.is_empty()
        if is_empty:
            str+= ']'
            return str

        cursor = self.__head
        count = 0
        while count < self.size:
            str += f'{cursor.data}, '
            cursor = cursor.next
            count += 1
        str = str[:-2] + " ]"
        return str
    
    @property
    def head(self):
        return self.__head
    
    @property
    def size(self):
        return self.__size
    
    @property
    def data_type(self):
        return self.__data_type
    
    @head.setter
    def head(self, new_head):
        self.__head = new_head
    
    @size.setter
    def size(self, new_size):
        self.__size = new_size
        
    @data_type.setter
    def data_type(self, new_data_type):
        self.__data_type = new_data_type
    
    def is_empty(self):
        '''
        Método para verificar se a estrutura de dados está vazia ou não.
        Ele retorna uma tupla (valor booliano indicando se está vazia ou não,
        mensagem de erro para ser exibido em uma exception)
        '''
        if self.__data_type != DataType.UNDEFINED:
            if self.__size == 0:
                return (True, f'A {self.__data_type.value} está vazia.')
            else:
                return (False, None)
            
    def check_position(self, position, plus=0):
        '''
        Método para verificar se a posição inserida é válida (existe ou não).
        Ele retorna uma tupla (valor booleano indicando se está válido ou não,
        mensagem de erro para ser exibido em uma exception)
        *Esse método possui um parâmetro `plus` com valor default igual a 0.
        Esse parâmetro é particularmente necessário para inserirmos um primeiro
        nó em uma lista vazia, só precisamos passar o valor 1 como argumento
        '''
        if position > 0 and position <= self.size + plus:
            return (True, None)
        else:
            return (False,
                    f'A posição inserida não existe na {self.__data_type.value}.')
        
    def validations(self, position=None):
        '''
        Método responsável pelas validações. Esse método verifica se a lista
        está vazia e se a posição é inválida, necessariamente nessa ordem.
        Caso alguma dessas validações esteja inválida, o método retorna uma
        mensagem para ser exibida em uma exception. Caso tudo esteja certo, a
        lista não esteja vazia e a posição seja válida, o método retorna um
        valor False.
        '''
        is_empty, except_msg = self.is_empty()
        if is_empty:
            return except_msg
        if position:
            position_validation, except_msg = self.check_position(position)
            if not position_validation:
                return except_msg
        return False
        
    def get_node(self, position, minus=0, is_insert=False):
        '''
        Método para buscar um nó por sua posição e retorná-lo
        *Esse método possui um parâmetro `minus` com valor default igual a 0.
        Esse parâmetro é particularmente necessário quando queremos buscar um
        nó N posições anterior ao nó da posição que estamos querendo
        '''
        validation = self.validations(
            position=(position - 1) if is_insert else None)
        # Se estamos inserindo na lista, precisamos buscar o Nó imediatamente
        # anterior a posição que estamos tentando inserir. Caso não estejamos
        # inserindo nada na lista, apenas buscando o nó pela posição, enviamos
        # False como argumento no parâmetro position
        if validation:
            if self.__data_type == DataType.LISTA:
                raise ListaException(validation)
            elif DataType.PILHA:
                raise PilhaException(validation)
        cursor = self.__head
        count = 1
        while cursor and count < (position - minus):
            cursor = cursor.next
            count += 1
        return cursor
    
    def search_by_value(self, value):
        '''
        Método para buscar um nó por valor e retornar sua posição.
        Obs.: caso existam nós com valores duplicados, esse método vai retornar
        apenas o primeiro a ser encontrado.
        '''
        validation = self.validations()
        if validation:
            if type == DataType.LISTA:
                raise ListaException(validation)
            elif DataType.PILHA:
                raise PilhaException(validation)

        cursor = self.__head
        count = 1

        while count <= self.size:
            if cursor.data == value:
                return count
            cursor = cursor.next
            count += 1
