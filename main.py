# Mosaico de Fotos de Satelite
# 
# Desenvolvido por Luiz Gustavo Sabadim Spolon Junqueira

import sys

caminho = sys.argv[1] # Pega o caminho para o arquivo de teste

retangulosIniciais = []
retangulosResultantes = []

# Abre o arquivo de teste e realiza a leitura linha a linha
# Adicionando os valores em uma lista
with open(caminho, 'r') as file:
    for line in file:
        retangulosIniciais.append(list(map(int, line.rstrip().split())))
        