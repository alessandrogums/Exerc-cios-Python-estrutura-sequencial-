#Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
from time import sleep

print('-'*30,'JOGO DO PEDRA, PAPEL E TESOURA','-'*30)
opcoes=int(input('opções:\n1)pedra '
                 '\n2)papel '
                 '\n3)tesoura '
                 '\nqual será sua escolha?'))
variaveis=('pedra','papel','tesoura')
lista_computador=(0,1,2)
print(len(lista_computador))
opcao_computador=choice(lista_computador)
print('-'*92)
sleep(2)
print('JO')
sleep(2)
print('KEEEEN')
sleep(2)
print('POOOO')
sleep(1)
print('-'*92)
print(f'voce escolheu:{variaveis[(opcoes)-1]} o computador escolheu: {variaveis[opcao_computador]}' )
if opcoes==1:
    if opcao_computador==0:
        print('deu empate!')
    elif opcao_computador==1:
        print('você perdeu, papel ganha de pedra hihihi')
    elif opcao_computador==2:
        print('você ganhou, tesoura perde de pedra :(')
elif opcoes==2:
    if opcao_computador==0:
        print('eu perdi , pedra perde de papel, naaaao')
    elif opcao_computador==1:
        print('deu empate!')
    elif opcao_computador==2:
        print('eu ganhei hehehehe, tesoura corta o papel em picadinhos kkkk')
elif opcoes==3:
    if opcao_computador==0:
        print('eu ganhei. Pedra amassa a tesoura.')
    elif opcao_computador==1:
        print('eu perdi :( sua tesoura me corta todinho')
    elif opcao_computador==2:
        print('deu empate!')
else:
    print('digitou um valor errado. Digite novamente!')
