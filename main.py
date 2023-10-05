from bomb import BombSimulator


def menu(content_data:list[str]=None):
    '''
    Método que exibe um menu de opções para o usuário
    '''
    options = [1, 2, 3]
    
    while True:
        print(
            '''
    --- Círculo da Bomba ---
    
    1 - Iniciar círculo da bomba
    2 - Créditos
    3 - Sair
    '''
        )
        try:
            choice = int(input('Escolha uma opção: '))
        except ValueError:
            continue
        if choice not in options:
            print('Digite uma opção válida.')
            continue
        elif choice == 1:
            new_simulation(content_data)
        elif choice == 2:
            show_credits()
        elif choice == 3:
            return


def new_simulation(content_data:list[str]=None):
    '''
    Método que prepara a simulação do círculo da bomba. Esse método pode receber uma
    lista de participantes, caso contrário, será necessário informar um a um antes
    de iniciar o jogo
    '''
    winners_num_error = 'O número de vencedores precisa ser maior que o de participantes'
    parti_name_error = 'O nome do participante deve ter ao menos dois caracteres.'
    parti_duplicated_error = 'já está participando.'
    if content_data and len(content_data) > 2:
        # se recebemos uma lista de participantes, devemos validar todos eles
        try:
            for item in content_data:
                # validamos se o nome do participante tem ao menos dois caracteres
                assert len(item) > 1, f'[{item}] -> {parti_name_error}'
                
                # validamos se o nome do participante não está duplicado
                assert content_data.count(item) == 1, f'{item} {parti_duplicated_error}'
        except AssertionError as e:
            # Caso seja encontrado algum erro, informamos que não pôde ser carregado
            # e o jogo prossegue para que o usuário possa inserir os participantes
            # de forma manual
            print(f'\n--- [ERRO] {e} ---\n--- [ERRO] O arquivo não pôde ser carregado ---\n')
            content_data = None
    while True:
        try:
            winners_num = int(
                input('Digite a quantidade de vencedores: '))
            # validamos que o número de vencedores inseridos é igual ou maior que 1
            assert winners_num >= 1, 'Deve ter ao menos um vencedor.'
            if content_data and len(content_data) > 2:
                # validamos se o número de vencedores inseridos é maior que o
                # número de participantes recebidos
                assert len(content_data) > winners_num, winners_num_error
            break
        except ValueError:
            print('Insira um valor válido.')
        except AssertionError as error:
            print(error)
    if not content_data or len(content_data) < 2:
        # se não recebermos participantes previamente, o programa segue para
        # a inserção manual da quantidade de participantes e seus respectivos nomes
        while True:
            try:
                participants_num = int(
                    input('Digite a quantidade de participantes: '))
                # validamos se o número de vencedores inseridos é maior que o
                # número de participantes recebidos
                assert participants_num > winners_num, 'O número de participantes deve ser maior que o de vencedores.'
                break
            except ValueError:
                print('Insira um valor válido.')
            except AssertionError as error:
                print(error)
        participants = []
        # Após receber a quantidade de participantes, o usuário insere o nome de cada um
        while len(participants) < participants_num:
            for i in range(participants_num):
                while True:
                    try:
                        participant = input(f'Digite o nome do participante [{i+1}/{participants_num}]: ')
                        assert len(participant) > 1, parti_name_error
                        assert participant not in participants, f'{participant} {parti_duplicated_error}'
                        participants.append(participant)
                        break
                    except AssertionError as error:
                        print(error)
    else:
        participants = content_data
    # início da simulação
    start_simulation(participants, winners_num)


def start_simulation(participants:list[str],
                     winners_num:int=None):
    '''
    Método que inicia a simulação do círculo da bomba. Esse método recebe os dados
    já validados e prontos para dar início ao jogo
    '''
    bomb = BombSimulator(participants=participants,
                         winners=winners_num)
    while bomb.winners < bomb.participants.size:
        summary = bomb.go()
        print(summary)
        input('Pressione uma tecla para continuar. ')
    # Uma vez que o número de participantes seja igual ao número de vencedores,
    # o jogo acabou e podemos exibir o(s) vencedor(es) e o caminho para vitória
    show_winners(bomb)


def show_winners(bomb:BombSimulator):
    '''
    Método para exibir o(s) vencedor(es) e o caminho para vitória
    '''
    winners = bomb.participants.__str__().replace(f"{bomb.participants.data_type.value.title()}: ", "")
    round = bomb.round
    removed_pile = bomb.removed_pile.__str__().replace(f"{bomb.removed_pile.data_type.value.title()}: ", "").replace(",", " <")
    print((f'\nVencedor(es) após {round} rodadas <<< {winners} >>>\n'
           f'Percurso para a vitória:\n{removed_pile}'))
    


def show_credits():
    '''
    Método para exibir os créditos
    '''
    print('''
    --- Círculo da Bomba ---
    
    Projeto elaborado para a disciplina de Estrutura de Dados,
    do curso de Sistemas Para Internet — IFPB, no semestre 2023.2
    
    Autores: Douglas Carneiro e Caue Trajano
    ''')
