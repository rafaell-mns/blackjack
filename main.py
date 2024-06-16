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
    nomes_cartas_jogador = []
    valores_cartas_jogador = []

    for i in range(5):  # Pega as primeiras 5 cartas do baralho para o jogador
        nome, valor = retorna_carta(baralho, i)
        nomes_cartas_jogador.append(nome)
        valores_cartas_jogador.append(valor)
    
    nomes_cartas_bot = []
    valores_cartas_bot = []

    for i in range(5, 10):  # Pega as próximas 3 cartas do baralho para o bot
        nome, valor = retorna_carta(baralho, i)
        nomes_cartas_bot.append(nome)
        valores_cartas_bot.append(valor)

    print("Valores das cartas do jogador:", valores_cartas_jogador)
    print("Valores das cartas do bot:", valores_cartas_bot)

    cartas_jogador = []
    for nome in nomes_cartas_jogador:
        caminho = f'imagens/cartas/{nome}'
        carta = pygame.image.load(caminho).convert_alpha()
        cartas_jogador.append(carta)

    cartas_bot = []
    for nome in nomes_cartas_bot:
        caminho = f'imagens/cartas/{nome}'
        carta = pygame.image.load(caminho).convert_alpha()
        cartas_bot.append(carta)

    return cartas_jogador, valores_cartas_jogador, cartas_bot, valores_cartas_bot

def calcular_valor_mao(valores_cartas, cartas_exibidas):
    valor_mao = sum(valores_cartas[:cartas_exibidas])
    return valor_mao

def renderizar_texto(screen, texto, posicao, tamanho=32, cor=(255, 255, 255)):
    fonte = pygame.font.Font(None, tamanho)
    texto_surface = fonte.render(texto, True, cor)
    text_rect = texto_surface.get_rect()
    text_rect.center = posicao  # Define o centro da caixa de texto
    screen.blit(texto_surface, text_rect)

def calcular_posicao_bot(index):
    pos_x = LARGURA_TELA - LARGURA_CARTA - MARGEM - index * (LARGURA_CARTA + ESPACO_ENTRE_CARTAS)
    pos_y = MARGEM
    return pos_x, pos_y

def main():
    screen = inicializar_pygame()
    background_img = carregar_fundo()
    baralho = criar_baralho()
    cartas_jogador, valores_cartas_jogador, cartas_bot, valores_cartas_bot = carregar_cartas_jogador(baralho)

    posicao_x = MARGEM
    posicao_y = ALTURA_TELA - ALTURA_CARTA - MARGEM
    cartas_exibidas = 2

    # Carregar a imagem "back" para as cartas do bot inicialmente
    back_image = pygame.image.load('imagens/astronaut.png').convert_alpha()
    cartas_bot_back = [back_image, back_image]

    mostrar_cartas_bot = False  # Estado para controlar a exibição das cartas do bot

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
                    cartas_jogador, valores_cartas_jogador, cartas_bot, valores_cartas_bot = carregar_cartas_jogador(baralho) # Carrega novas cartas para o jogador e para o bot
                    cartas_exibidas = 2 # Reinicia a exibição para 2 cartas
                    mostrar_cartas_bot = False  # Reiniciar estado das cartas do bot
                elif event.key == pygame.K_c:  # Pressione 'c' para mostrar as cartas do bot
                    mostrar_cartas_bot = True

        screen.blit(background_img, (0, 0))

        # Desenhar as cartas bot no canto superior direito
        if mostrar_cartas_bot:
            for i, carta in enumerate(cartas_bot):
                pos_x_bot, pos_y_bot = calcular_posicao_bot(i)
                screen.blit(carta, (pos_x_bot, pos_y_bot))
        else:
            for i, carta in enumerate(cartas_bot_back):
                pos_x_bot, pos_y_bot = calcular_posicao_bot(i)
                screen.blit(carta, (pos_x_bot, pos_y_bot))

        # Exibir as cartas de acordo com quantas já foram mostradas
        for i in range(cartas_exibidas):
            screen.blit(cartas_jogador[i], (posicao_x + i * (LARGURA_CARTA + ESPACO_ENTRE_CARTAS), posicao_y))

        valor_mao = calcular_valor_mao(valores_cartas_jogador, cartas_exibidas)
        renderizar_texto(screen, f"Valor da Mão: {valor_mao}", (LARGURA_TELA//2, ALTURA_TELA//2))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
