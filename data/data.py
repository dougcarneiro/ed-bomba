import re


def read_file(file_path: str) -> list[str] or None:
    '''
    Método para ler um arquivo externo e recuperar uma lista de participantes.
    Obs.: garanta que os participantes estejam devidamente separados por vírgula
        dentro do arquivo externo.
    '''
    formatted_content = []
    try:
        with open(file_path, 'r') as arquivo:
            content = arquivo.read().split(',')
            for item in content:
                formatted_content.append(re.sub(r'[^a-zA-Z0-9À-ÿ]', '', item))
    except FileNotFoundError:
        print(f"O arquivo '{file_path}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")
    
    return formatted_content if formatted_content else None
