#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa=float(input('digite o valor da casa:R$'))
salario_mensal=float(input('qual seu salário mensal?R$'))
tempo_pagamento=int(input('quanto tempo pretende pagar a casa, em anos ?'))
prestacao=(casa/(tempo_pagamento*12))
print(f'o valor da prestação é de  R$ {prestacao}')
if  prestacao <= 0.3 * salario_mensal:
  print(' voce  poderá fazer um empréstimo')
else:
print(' voce não poderá realizar o emprestimo')

aprovando empréstimo(segundo jeito)
casa=float(input(' valor da casa é: '))
salario=float(input(' digite seu salário'))
tempo_anos=int(input(' digite em quantos anos quer pagar?'))
tempo_100=int(casa/salario)
emprestimo=0.3*salario
tempo_30=int(casa/emprestimo)
print(tempo_30)
if tempo_30 <= tempo_anos * 12:
 print(' voce  poderá fazer o empréstimo')
else:
print(' voce  n poderá fazer o empréstimo')
