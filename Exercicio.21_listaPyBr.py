#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
#As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
#O valor mínimo é de 10 reais e o máximo de 600 reais. 
#O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
valor = int(input('digite o valor que você quer retirar do caixa eletrônico=R$ '))
notas_1 = notas_5 = notas_10 = notas_50 = notas_100 = 0
if valor >= 10 and valor <= 600:
    while valor >= 100:
        valor -= 100
        notas_100 += 1
    while valor >= 50:
        valor -= 50
        notas_50 += 1
    while valor >= 10:
        valor -= 10
        notas_10 += 1
    while valor >= 5:
        valor -= 5
        notas_5 += 1
    while valor >= 1:
        valor -= 1
        notas_1 += 1
print(f'você receberá:'
        f'\n{notas_100} notas de R$100 '
        f'\n{notas_50} notas  de R$50 '
        f'\n{notas_10} notas  de R$10 '
        f'\n{notas_5}  notas  de R$5  '
        f'\n{notas_1}  notas  de R$1   ')
