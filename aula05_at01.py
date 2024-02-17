from os import system
system('cls')

def Soma(numero1, numero2):
    try:
        print('A soma dos numero é {}'.format(float(numero1) + float(numero2)))
    except:
        print('error...')

def Subtrair(numero1, numero2):
    print('A subtraçao dos numero é {}'.format(numero1 - numero2))

def Multiplicacao(numero1, numero2):
    print('A multiplicação dos numero é {}'.format(numero1 * numero2))

def Divisao(numero1, numero2):
    try:
        print('A divisão dos numero é {}'.format(numero1 / numero2))
    except ZeroDivisionError as error:
        print(error)
    except:
        print('Algo deu muito errado')
    

while True:
    num1 = input('digite o primeiro numero: ')
    num2 = input('digite o segundo numero: ')

    print('1. Soma')
    print('2. Subtrair')
    print('3. Multiplicação')
    print('4. Divisão')

    opcao = int(input('Opção: '))
    if opcao == 1:
        Soma(num1, num2)
    if opcao == 2:
        Subtrair(num1, num2)
    if opcao == 3:
        Multiplicacao(num1, num2)
    if opcao == 4:
        Divisao(num1, num2)

