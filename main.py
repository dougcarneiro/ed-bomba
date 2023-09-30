from bomb import BombSimulator


def menu(content_data=None):
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


def new_simulation(content_data=None):
    winners_num_error = 'O número de vencedores não pode ser maior que o de participantes'
    parti_name_error = 'O nome do participante deve ter ao menos dois caracteres.'
    parti_duplicated_error = 'já está participando.'
    if content_data and len(content_data) > 1:
        try:
            for item in content_data:
                assert len(item) > 1, f'[{item}] -> {parti_name_error}'
                assert content_data.count(item) == 1, f'{item} {parti_duplicated_error}'
        except AssertionError as e:
            print(f'\n--- [ERRO] {e} ---\n--- [ERRO] O arquivo não pôde ser carregado ---\n')
            content_data = None
    while True:
        try:
            winners_num = int(
                input('Digite a quantidade de vencedores: '))
            assert winners_num >= 1, 'Deve ter ao menos um vencedor.'
            if content_data:
                assert len(content_data) > winners_num, winners_num_error
            break
        except ValueError:
            print('Insira um valor válido.')
        except AssertionError as error:
            print(error)
    if not content_data or len(content_data) < 1:
        while True:
            try:
                participants_num = int(
                    input('Digite a quantidade de participantes: '))
                assert participants_num > winners_num
                break
            except ValueError:
                print('Insira um valor válido.')
        participants = []
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
    start_simulation(participants, winners_num)


def start_simulation(participants,
                     winners_num=None):
    bomb = BombSimulator(participants=participants,
                         winners=winners_num)
    while bomb.winners < bomb.participants.size:
        bomb.go()
        input('Pressione uma tecla para continuar. ')

    show_winners(bomb)


def show_winners(bomb):
    winners = bomb.participants.__str__().replace(f"{bomb.participants.data_type.value.title()}: ", "")
    round = bomb.round
    removed_pile = bomb.removed_pile.__str__().replace(f"{bomb.removed_pile.data_type.value.title()}: ", "").replace(",", " <")
    print((f'\nVencedor(es) após {round} rodadas <<< {winners} >>>\n'
           f'Percurso para a vitória:\n{removed_pile}'))
    


def show_credits():
    print('''
    --- Círculo da Bomba ---
    
    Projeto elaborado para a disciplina de Estrutura de Dados,
    do curso de Sistemas Para Internet — IFPB, no semestre 2023.2
    
    Autor: Douglas Carneiro
    ''')
