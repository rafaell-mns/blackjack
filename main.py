import pygame
import sys
from jogo import *

# Constantes
LARGURA_TELA = 740
ALTURA_TELA = 503
LARGURA_CARTA = 117
ALTURA_CARTA = 166
MARGEM = 35
ESPACO_ENTRE_CARTAS = 20  # Espaço entre cada carta

def inicializar():
    pygame.init()
    screen = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('Jogo')
    background_img = pygame.image.load('imagens/board.png').convert()
    return screen, background_img

def carregar_cartas():
    nomes_cartas = []
    
    for i in range(5):
        nome = retorna_carta() # sorteia a carta
        nomes_cartas.append(nome)

    # Lista para armazenar as superfícies das cartas
    cartas = []

    # carregas as cartas sorteadas
    for nome in nomes_cartas:
        caminho = f'imagens/cartas/{nome}'
        carta = pygame.image.load(caminho).convert_alpha()
        cartas.append(carta)

    return cartas

def main():
    screen, fundo = inicializar()
    cartas = carregar_cartas()

    # Posição inicial das primeiras cartas
    posicao_x = MARGEM
    posicao_y = ALTURA_TELA - ALTURA_CARTA - MARGEM

    # Variável para controlar quantas cartas foram exibidas
    cartas_exibidas = 2

    # Loop principal
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if cartas_exibidas < 5:  # Mostra até a 5ª carta
                        cartas_exibidas += 1

        # Desenhar imagem de fundo (tabuleiro)
        screen.blit(fundo, (0, 0))

        # Exibir as cartas de acordo com quantas já foram mostradas
        for i in range(cartas_exibidas):
            screen.blit(cartas[i], (posicao_x + i * (LARGURA_CARTA + ESPACO_ENTRE_CARTAS), posicao_y))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
