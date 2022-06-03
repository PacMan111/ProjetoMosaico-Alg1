'''
   Programa: mosaico.py
        Função: Gerar um mosaico a partir de coordenadas de retângulos fornecidas.

        Uso: python mosaico.py <caminho para o arquivo de teste> <opcao de desenhar o resultado>

                Na parte da opção de desenhar o resultado, inserir "True" ou "true" para desenhar
                ou deixar em branco para não desenhar.

        Programador: Luiz Gustavo Sabadim Spolon Junqueira
       Data: 02/06/2022.
'''

import sys 
from utils import calcular, printarResultados, desenharResultados

caminho = sys.argv[1] # Pega o caminho para o arquivo de teste

#Realiza o calculo dos mosaicos e armazena na variavel resultados
resultados = calcular(caminho)

# Mostra os resultados na tela
printarResultados(resultados)

#Se tiver ativado para desenhar, instancia a janela e desenha os retangulos
if len(sys.argv) > 2 and sys.argv[2].lower() == "true":
    desenharResultados(resultados)