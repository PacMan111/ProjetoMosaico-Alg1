# Mosaico de Fotos de Satelite
# 
# Desenvolvido por Luiz Gustavo Sabadim Spolon Junqueira

import sys 
import random
import pygame
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

# Mostra os resultados na tela
for r in resultadoFinal:
    ut.printarRetangulo(r)

size = width, height = 1080, 720

screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))

for res in resultadoFinal:
    xse, yse, xid, yid = res
    largura = xid - xse
    altura = yse - yid

    rect = pygame.Rect(xse, yid, largura, altura)
    pygame.draw.rect(screen, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), rect) 

screen.blit(pygame.transform.flip(screen, False, True), dest=(0, 0))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit() 

    pygame.display.flip()