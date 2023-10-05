import argparse

from main import menu
from data.data import read_file


# caminho do arquivo com os participantes já preenchidos
FILE_PATH = 'data/participants_data.txt'


parser = argparse.ArgumentParser(prog='círculo-da-bomba',
                                     description=('Simulação do Círculo da Bomba'),
                                     add_help=True)
parser.add_argument('--file', '-f')
args = parser.parse_args()

content_data = read_file(FILE_PATH if not args.file else args.file)

try:
    menu(content_data)
except KeyboardInterrupt:
    print('\nTchauzinho... :)')
