import pygame
import sys 

# Printar o retangulo formatado
def printFormatado(ret):
    print(f"({ret[0]},{ret[1]}), ({ret[2]},{ret[3]})")

#Printa a quantidade de resultados e eles em seguida
def printarResultados(res):
    print(len(res))
    for r in res:
        printFormatado(r)
    
# Abre o arquivo de teste e realiza a leitura linha a linha
# Adicionando os valores em uma lista e retorna ela
def lerArquivo(caminho):
    with open(caminho, 'r') as file:            
        return [list(map(int, line.rstrip().split())) for line in file]

# Funcao para fazer a comparacao entre dois retangulos e retornar um resultante, ou os dois iniciais
def compararRetangulos(ret1, ret2):
    xSe, ySe, xId, yId = ret1 # Posicoes do retangulo 1
    xSe2, ySe2, xId2, yId2 = ret2 # Posicoes do retangulo 2

    intervaloX = False
    intervaloY = False

    # Verifica se os retangulos se intersectam no eixo X
    if (xSe <= xSe2 <= xId or xSe2 <= xId <= xId2) or (xSe2 <= xSe <= xId2 or xSe <= xId2 <= xId):
        intervaloX = True
    
    # Verifica se os retangulos se intersectam no eixo Y
    if (yId <= ySe2 <= ySe or yId2 <= yId <= ySe2) or (yId2 <= ySe <= ySe2 or yId <= yId2 <= ySe):
        intervaloY = True
        
    if intervaloX and intervaloY:
        # Pega os valores correspondentes as posicoes do retangulo resultante
        menorXSe = min(xSe, xSe2)
        maiorYSe = max(ySe, ySe2)
        maiorXid = max(xId, xId2)
        menorYid = min(yId, yId2)

        #Retorna o retangulo resultante       
        return [[menorXSe, maiorYSe, maiorXid, menorYid]]
    else:
        #Retorna os retangulos iniciais se eles não houver sobreposição
        return [ret1, ret2]

#Função para calcular os retangulos resultantes de uma lista de retangulos
def gerarMosaicos(retangulos):

    if len(retangulos) > 1: 
        resultado = compararRetangulos(retangulos[0], retangulos[1])

        #Variável de contagem pro loop nos resultados
        countResultado = 0
        countResultadoAnterior = 0

        #Faz um loop por todos os resultados
        while countResultado < len(resultado):

            #Variável de contagem pro loop nos retangulos
            countRetangulos = 0

            # Faz um loop por todos os retangulos
            while countRetangulos < len(retangulos):                
                #Faz a comparacao entre o resultado e o retangulo
                comparacao = compararRetangulos(resultado[countResultado], retangulos[countRetangulos])

                # Adiciona os novos resultados
                for r in comparacao:
                    if r not in resultado:
                        resultado.append(r)

                # Se o retangulo da lista de resultados não estiver na comparacao, remove ele dos retangulos resultantes
                if resultado[countResultado] not in comparacao:
                    resultado.remove(resultado[countResultado])
                    # #Pra garantir que só diminui uma vez, para manter a posição na lista
                    if countResultadoAnterior == countResultado:
                        countResultado -= 1
                    
                # Se o retangulo da lista de retangulos não estiver na comparação, remove ele da lista de retangulos
                # Os ifs são separados pois não é só porque um não está que o outro está errado, ja que um pode estar dentro do outro
                if retangulos[countRetangulos] not in comparacao:
                    retangulos.remove(retangulos[countRetangulos])
                    countRetangulos -= 1
                    
                countRetangulos += 1

            countResultado += 1
            countResultadoAnterior = countResultado


    else: # Se só tiver um retangulo, não precisa comparar então retorna ele
        resultado = retangulos

    return resultado

#Função para fazer o calculo dos mosaicos
def calcular(caminho):
    resultadoAnterior = []
    resultadoFinal = gerarMosaicos(lerArquivo(caminho))

    # Repete o calculo até que o novo resultado seja igual ao anterior,
    # para garantir que o resultado não possua retangulos com sobreposição
    while resultadoAnterior != resultadoFinal:
        resultadoAnterior = resultadoFinal
        resultadoFinal = gerarMosaicos(resultadoAnterior)

    return resultadoFinal

def definirEscala(resultados):
    maiorLargura = max([(xid - xse) for xse, _, xid, _ in resultados])
    maiorAltura = max([(yse - yid) for _, yse, _, yid in resultados])


    escala = (1080 / maiorLargura + 720 / maiorAltura) / 10

    escala = 1 if (escala<1) else escala

    print(escala)

    return escala

def desenharResultados(resultados):
    size = 1080, 720

    escala = definirEscala(resultados)

    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))

    for res in resultados:
        xse, yse, xid, yid = [v*escala + 5 for v in res]
        largura = xid - xse
        altura = yse - yid

        rect = pygame.Rect(xse, yid, largura, altura)
        pygame.draw.rect(screen, (0, 0, 0), rect) 

    for i in range(2, int(1080/(escala*5))):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(i * escala * 5, 0, 1, 5))
    
    for i in range(2, int(720/(escala*5))):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, i * escala * 5, 5, 1))

    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(5, 0, 1, 720))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, 5, 1080, 1))

    screen.blit(pygame.transform.flip(screen, False, True), dest=(0, 0))

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit() 

        pygame.display.flip()