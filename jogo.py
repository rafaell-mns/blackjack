import random

def retorna_carta():
    valores = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    naipes = ['Hearts', 'Spades', 'Diamonds', 'Clubs']

    baralho = [(valor, naipe) for naipe in naipes for valor in valores]

    # Embaralhar o baralho
    random.shuffle(baralho)

    # Sortear uma carta aleatória
    carta_sorteada = random.choice(baralho)
    valor_carta, naipe_carta = carta_sorteada

    # Gerar o nome do arquivo para a carta sorteada
    nome_do_arquivo = f"{naipe_carta.lower()}_{valor_carta.lower()}.png"

    print(f"Carta sorteada: {valor_carta} de {naipe_carta}")
    print(f"Nome do arquivo: {nome_do_arquivo}")

    return nome_do_arquivo

# criar função que retorna só o valor da carta