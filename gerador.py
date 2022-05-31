'''
   Programa: gerador.py
     Função: Gerar uma sequência de retângulos identificados pelas suas coordenadas
             do canto superior esquerdo (x_se, y_se) e do canto inferior direito
             (x_id, y_id). Os valores do tamanho da base e da altura, bem como o
             total de pontos a serem gerados são passados como parâmetros por
             linha de comando.
        Uso: python gerador.py <base> <altura> <qtd_areas>
Programador: Amaury Antônio de Castro Junior
       Data: 29/5/2022.
'''

# Módulos usados para gerar números aleatórios e permitir a passagem de
# parâmtros por linha de comando.
import random
import sys

# Armazena os valores de <base> e <altura> passados por linha de comando.
base = int(sys.argv[1])
altura = int(sys.argv[2])

# Armazena o valor da quantidade de areas a serem lidas, passado por linha
# de comando
num_areas = int(sys.argv[3])

# Inicializa os valores das coordenadas que identificam uma área
x_se = y_se = x_id = y_id = 0

# Inicializa o valor de áreas válidas. As áreas válidas devem possuem
# coordenadas (x_se, y_se) e (x_id, y_id), tal que (x_se < y_id) E (y_se > y_id)
areas_validas = 0

# Laço para geração dos valores das coordenadas que identificam as áreas
# Devem ser geradas <num_areas> coordenadas.
while areas_validas < num_areas:

    # Geração aleatória dos valores das coordenadas
    x_se = random.randint(0,base)
    y_se = random.randint(0,altura)
    x_id = random.randint(0,base)
    y_id = random.randint(0,altura)

    # Verifica se as coordenadas geradas são válidas, de acordo com os
    # critérios de entrada definidos para o projeto.
    if (x_se < x_id and y_se > y_id):

        # Se forem válidas, imprime as coordenadas e incrementa o contador
        # de áreas válidas
        print("%i %i %i %i"%(x_se,y_se,x_id,y_id))
        areas_validas += 1

  
