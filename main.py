# Mosaico de Fotos de Satelite
# 
# Desenvolvido por Luiz Gustavo Sabadim Spolon Junqueira

import sys

# Printar o retangulo formatado
def printarRetangulo(ret):
    print(f"({ret[0]},{ret[1]}), ({ret[2]},{ret[3]})")
    
# Abre o arquivo de teste e realiza a leitura linha a linha
# Adicionando os valores em uma lista e retorna ela
def lerArquivo(caminho):
    retangulos = []
    
    with open(caminho, 'r') as file:
        for line in file:
            ret = list(map(int, line.rstrip().split()))
            retangulos.append(ret) 
            
    return retangulos

# Funcao para fazer a comparacao entre dois retangulos e retornar um resultante, ou os dois iniciais
def criarMosaico(ret1, ret2):
    xSe, ySe, xId, yId = ret1 # Posicoes do retangulo 1
    xSe2, ySe2, xId2, yId2 = ret2 # Posicoes do retangulo 2
    retorno = []
    
    menorXSe, maiorXid = 0, 0
    maiorYSe, menorYid = 0, 0
    
    if xSe < xSe2:
        menorXSe = xSe
    else:
        menorXSe = xSe2
    if xId < xId2:
        maiorXid = xId2
    else:
        maiorXid = xId
        
    if ySe > ySe2:
        maiorYSe = ySe
    else:
        maiorYSe = ySe2
    if yId < yId2:
        menorYid = yId
    else:
        menorYid = yId2

    intervaloX = False
    intervaloY = False

    if (xSe <= xSe2 <= xId or xSe2 <= xId <= xId2) or (xSe2 <= xSe <= xId2 or xSe <= xId2 <= xId):
        intervaloX = True
    
    if (yId <= ySe2 <= ySe or yId2 <= yId <= ySe2) or (yId2 <= ySe <= ySe2 or yId <= yId2 <= ySe):
        intervaloY = True
        
    if intervaloX and intervaloY:
        retorno.append([menorXSe, maiorYSe, maiorXid, menorYid])
    else:
        retorno.append(ret1)
        retorno.append(ret2)
        
    return retorno
 
caminho = sys.argv[1] # Pega o caminho para o arquivo de teste

# Armazena os retangulos de teste
retangulosIniciais = lerArquivo(caminho)

# Calcula o resultado da combinacao dos dois primeiros triangulos
retangulosResultantes = criarMosaico(retangulosIniciais[0], retangulosIniciais[1])
    
# Para cada triangulo alem dos dois primeiros, compara com os resultados anteriores
for i in range(2, len(retangulosIniciais)):
    
    # Compara com cada um dos resultados anteriores
    for ret in retangulosResultantes:
        rets = criarMosaico(ret, retangulosIniciais[i])
        
        #Se o resultado anterior estiver no novo resultado, remove ele
        if ret in rets:
            rets.remove(ret)
        else:
            # Se nao, remove o resultado anterior dos retangulos resultantes, ja que ele nao é mais verdadeiro
            retangulosResultantes.remove(ret) 
            
    # Adiciona os novos resultados
    for r in rets:
        retangulosResultantes.append(r)
        
print(len(retangulosResultantes))
        
for ret in retangulosResultantes:
    printarRetangulo(ret)