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

    intervaloX = False
    intervaloY = False

    if (xSe <= xSe2 <= xId or xSe2 <= xId <= xId2) or (xSe2 <= xSe <= xId2 or xSe <= xId2 <= xId):
        intervaloX = True
    
    if (yId <= ySe2 <= ySe or yId2 <= yId <= ySe2) or (yId2 <= ySe <= ySe2 or yId <= yId2 <= ySe):
        intervaloY = True
        
    if intervaloX and intervaloY:
        # Pega os valores correspondentes as posicoes do retangulo resultante
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
                
        return [[menorXSe, maiorYSe, maiorXid, menorYid]]
    else:
        return [ret1, ret2]

def calcular(iniciais):

    if len(iniciais) > 1:
        # Calcula o resultado da combinacao dos dois primeiros triangulos
        resultado = criarMosaico(iniciais[0], iniciais[1])

        # Para cada triangulo alem dos dois primeiros, compara com os resultados anteriores
        for i in range(2, len(iniciais)):
            
            # Compara com cada um dos resultados anteriores
            for ret in resultado:
                comparacao = criarMosaico(ret, iniciais[i])
               
                # Se o resultado anterior não estiver na comparacao, remove ele dos retangulos resultantes
                if ret not in comparacao:
                    resultado.remove(ret) 

                # Adiciona os novos resultados
                for r in comparacao:
                    if r not in resultado:
                        resultado.append(r)
    else:
        resultado = iniciais

    return resultado