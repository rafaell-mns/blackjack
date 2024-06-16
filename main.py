import pygame
import sys
from jogo import *

# Constantes do jogo
LARGURA_TELA = 740
ALTURA_TELA = 503
LARGURA_CARTA = 117
ALTURA_CARTA = 166
MARGEM = 35
ESPACO_ENTRE_CARTAS = 20

def inicializar_pygame():
    pygame.init()
    return pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

def carregar_fundo():
    return pygame.image.load('imagens/board.png').convert()

def carregar_cartas_jogador(baralho):
    nomes_cartas = []
    valores_cartas = []

    for i in range(5):  # Pega as primeiras 5 cartas do baralho
        nome, valor = retorna_carta(baralho, i)
        nomes_cartas.append(nome)
        valores_cartas.append(valor)
    
    print(valores_cartas)

    cartas_jogador = []
    for nome in nomes_cartas:
        caminho = f'imagens/cartas/{nome}'
        carta = pygame.image.load(caminho).convert_alpha()
        cartas_jogador.append(carta)

    return cartas_jogador, valores_cartas

def calcular_valor_mao(valores_cartas, cartas_exibidas):
    valor_mao = sum(valores_cartas[:cartas_exibidas])
    return valor_mao

def renderizar_texto(screen, texto, posicao, tamanho=32, cor=(255, 255, 255)):
    fonte = pygame.font.Font(None, tamanho)
    texto_surface = fonte.render(texto, True, cor)
    text_rect = texto_surface.get_rect()
    text_rect.center = posicao  # Define o centro da caixa de texto
    screen.blit(texto_surface, text_rect)

def main():
    screen = inicializar_pygame()
    background_img = carregar_fundo()
    baralho = criar_baralho()
    cartas_jogador, valores_cartas = carregar_cartas_jogador(baralho)

    posicao_x = MARGEM
    posicao_y = ALTURA_TELA - ALTURA_CARTA - MARGEM
    cartas_exibidas = 2

    # Loop principal do jogo
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if cartas_exibidas < 5:  # Mostra até a 5ª carta
                        cartas_exibidas += 1
                elif event.key == pygame.K_r:  # Pressione 'r' para reiniciar
                    baralho = baralho[cartas_exibidas:] + baralho[:cartas_exibidas] # Move as cartas retiradas para o final do baralho
                    cartas_jogador, valores_cartas = carregar_cartas_jogador(baralho) # Carrega novas cartas para o jogador
                    cartas_exibidas = 2 # Reinicia a exibição para 2 cartas

        screen.blit(background_img, (0, 0))

        # Exibir as cartas de acordo com quantas já foram mostradas
        for i in range(cartas_exibidas):
            screen.blit(cartas_jogador[i], (posicao_x + i * (LARGURA_CARTA + ESPACO_ENTRE_CARTAS), posicao_y))

        valor_mao = calcular_valor_mao(valores_cartas, cartas_exibidas)
        renderizar_texto(screen, f"Valor da Mão: {valor_mao}", (LARGURA_TELA//2, ALTURA_TELA//2))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
