#importanto o módulo aleatório
from random import randint

#importando o módulo de tempo para cadenciar o JOKENPÔ
from time import sleep

#definindo os itens
itens = ('Pedra', 'Papel', 'Tesoura', 'Lagarto', 'Spock')

#jogada do computador
computador = randint(0,4)

#apresentar opções
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura
[3] Lagarto
[4] Spock''')

#inserir jogada do jogador
jogador = int(input('Qual é a sua jogada?'))

#determinando tempo de execução para a resposta
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(2)
print('-=' * 11)

#mostrando as jogadas
print(f'Computador jogou: {[itens[computador]]}')
print(f'Jogador jogou: {[itens[jogador]]}')
print('-=' * 11)

#realizando as condicionais dos resultados
if computador == 0: #computador jogou Pedra
    if jogador == 0:
        print('EMPATE')

    elif jogador == 1:
        print('JOGADOR VENCEU!')

    elif jogador == 2:
        print('COMPUTADOR VENCEU!')
    
    elif jogador == 3:
        print('COMPUTADOR VENCEU!')

    elif jogador == 4:
        print('JOGADOR VENCEU!')

    else:
        print('Jogada Inválida!')

if computador == 1: #computador jogou Papel
    if jogador == 0:
        print('COMPUTADOR VENCEU!')

    elif jogador == 1:
        print('EMPATE')

    elif jogador == 2:
        print('JOGADOR VENCEU!')
    
    elif jogador == 3:
        print('COMPUTADOR VENCEU!')

    elif jogador == 4:
        print('COMPUTADOR VENCEU!')

    else:
        print('Jogada Inválida!')

if computador == 2: #computador jogou Tesoura
    if jogador == 0:
        print('JOGADOR VENCEU!')

    elif jogador == 1:
        print('COMPUTADOR VENCEU!')

    elif jogador == 2:
        print('EMPATE')
    
    elif jogador == 3:
        print('COMPUTADOR VENCEU!')

    elif jogador == 4:
        print('JOGADOR VENCEU!')

    else:
        print('Jogada Inválida!')

if computador == 3: #computador jogou Lagarto
    if jogador == 0:
        print('COMPUTADOR VENCEU!')

    elif jogador == 1:
        print('JOGADOR VENCEU!')

    elif jogador == 2:
        print('JOGADOR VENCEU!')
    
    elif jogador == 3:
        print('EMPATE')

    elif jogador == 4:
        print('COMPUTADOR VENCEU!')

    else:
        print('Jogada Inválida!')

if computador == 4: #computador jogou Pedra
    if jogador == 0:
        print('COMPUTADOR VENCEU!')

    elif jogador == 1:
        print('JOGADOR VENCEU!')

    elif jogador == 2:
        print('COMPUTADOR VENCEU!')
    
    elif jogador == 3:
        print('JOGADOR VENCEU!')

    elif jogador == 4:
        print('EMPATE')

    else:
        print('Jogada Inválida!')