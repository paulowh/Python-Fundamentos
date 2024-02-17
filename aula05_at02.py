import random
from os import system

def escolher_palavra():
    palavras = ['python', 'java', 'ruby', 'javascript', 'html', 'css', 'php']
    return random.choice(palavras)

def mostrar_palavra(palavra ,letras_escolhidas):
    exibicao = ''
    for letra in palavra:
        if letra in letras_escolhidas:
            exibicao += letra
        else:
            exibicao += '_'
    return exibicao

def jogar():
    system('cls')
    palavra_secreta = escolher_palavra()
    tentativas_restante = 6
    letras_escolhidas = []

    print('Bem vindo ao jogo da forca da galerinha...')
    print('Adivinhe a palavra secreta')
    print(mostrar_palavra(palavra_secreta, letras_escolhidas))

    while tentativas_restante > 0:
        letra = input('Digite uma letra: ').lower()

        if len(letra) != 1 or letra.isnumeric():
            print("por favor, digite apenas uma letra.")
            continue
        
        if letra in letras_escolhidas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        letras_escolhidas.append(letra) #adiciona a informação a lista

        if letra not in palavra_secreta:
            tentativas_restante = tentativas_restante - 1 # tentativas_restante -= 1
            print('Letra incorreta. Você tem {} tentativas restantes.'.format(tentativas_restante))
        else:
            print('Letra correta!')

        palavra_mostrar = mostrar_palavra(palavra_secreta, letras_escolhidas)
        print(palavra_mostrar)
        
        if palavra_mostrar == palavra_secreta:
            print('Você acertou!!!')
            break
    
    if tentativas_restante == 0:
        print('Você perdeu! ')

# 1- verificar se a LETRA já foi digitada
# 2- criar um laço para o usuario continuar a jogar 

op = ''
while op.upper() != 's':
    jogar()

    op = input('digite S para sair: ')
