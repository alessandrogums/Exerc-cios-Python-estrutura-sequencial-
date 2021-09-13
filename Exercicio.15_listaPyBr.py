#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
#Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

lado_1=int(input('digite o valor do suposto primeiro lado:'))
lado_2=int(input('digite o valor do suposto segundo lado:'))
lado_3=int(input('digite o valor do suposto terceiro lado:'))
if lado_1<lado_2+lado_3 and lado_2<lado_1+lado_3 and lado_3<lado_1+lado_2:
    print('os 3 lados formam um triângulo')
    
    if lado_1==lado_2==lado_3:
        print('e o triângulo é do tipo equilátero', end=' ')
    
    elif lado_1==lado_2!=lado_3 or lado_2==lado_3!=lado_1 or lado_1==lado_3!=lado_2:
        print('e o triângulo é do tipo isósceles', end=' ')
    else:
        print('e o triângulo é do tipo escaleno', end=' ')
else:
    print('os 3 lados não formam um triângulo')
