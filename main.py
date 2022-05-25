# Mosaico de Fotos de Satelite
# 
# Desenvolvido por Luiz Gustavo Sabadim Spolon Junqueira

import sys 
import utils as ut

caminho = sys.argv[1] # Pega o caminho para o arquivo de teste

# Armazena os retangulos iniciais
retangulosIniciais = ut.lerArquivo(caminho)

resultadoAnterior = []
resultadoFinal = ut.calcular(retangulosIniciais)

# Repete o calculo até que o novo resultado seja igual ao anterior
while resultadoAnterior != resultadoFinal:
    resultadoAnterior = resultadoFinal
    resultadoFinal = ut.calcular(resultadoAnterior)

for r in resultadoFinal:
    ut.printarRetangulo(r)