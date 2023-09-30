import re


def read_file(file_path):
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
