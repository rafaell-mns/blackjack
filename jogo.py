import random

def retorna_carta(baralho, indice):
    valor_carta, naipe_carta = baralho[indice]

    nome_do_arquivo = f"{naipe_carta.lower()}_{valor_carta.lower()}.png"
    print(nome_do_arquivo)

    valor_carta = valor_numerico(valor_carta)

    return nome_do_arquivo, valor_carta

def valor_numerico(nome):
    if nome == 'Ace':
        return 1
    elif nome == 'Jack':
        return 11
    elif nome == 'Queen':
        return 12
    elif nome == 'King':
        return 13
    else:
        return int(nome)


def criar_baralho():
    valores = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    naipes = ['Hearts', 'Spades', 'Diamonds', 'Clubs']

    baralho = [(valor, naipe) for naipe in naipes for valor in valores]
    random.shuffle(baralho)

    return baralho