import random
from words import words

def validacao_palavras(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word = validacao_palavras(words)
    word_letras = set(words)
    alfabeto = set(string.ascii_uppercase)
    letras_usadas = set()


    user_letra = input('Escolha uma letra: ').upper()


jogador_input = input('Escolha uma letra: ')
print(jogador_input)