#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário
#bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa
#que deposita). 
#O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
valor_hora = float(input('digite o valor da hora trabalhada-R$:'))
tempo = int(input('qual foi a quantidade de horas trabalhadas por mês?'))
salario_bruto = valor_hora * tempo
# Calcular o valor do Imposto de Renda(IR):
IR = 0
INSS = 0
FGTS = 0.11 * salario_bruto
if salario_bruto <= 900:
    IR = 0
    INSS = salario_bruto * 0.075
    print(f'Salário Bruto:             R${salario_bruto}'
          '\n(-)IR(0%) :               R${isento}'
          f'\n(-)INSS(7.5%)            R${INSS}'
          f'\n( )FGTS(11%)             R${FGTS}'
          f'\n   Total de descontos    R${IR + INSS}'
          f'\n   Salário Líquido       R${salario_bruto - (IR + INSS)}')
elif salario_bruto <= 1500:
    IR = salario_bruto * 0.05
    INSS = salario_bruto * 0.09
    FGTS = salario_bruto * 0.11
    print(print(f'Salário Bruto:          R${salario_bruto}'
                f'\n(-)IR(5%) :              R${IR}'
                f'\n(-)INSS(9%)              R${INSS}'
                f'\n( )FGTS(11%)             R${FGTS}'
                f'\n   Total de descontos    R${IR + INSS}'
                f'\n   Salário Líquido       R${salario_bruto - (IR + INSS)}'))
elif salario_bruto <= 2500:
    IR = salario_bruto * 0.1
    INSS = salario_bruto * 0.1
    FGTS = salario_bruto * 0.11
    print(print(f'Salário Bruto:         R${salario_bruto}'
                f'\n(-)IR(10%) :           R${IR}'
                f'\n(-)INSS(10%)           R${INSS}'
                f'\n( )FGTS(11%)           R${FGTS}'
                f'\n   Total de descontos  R${IR + INSS}'
                f'\n   Salário Líquido     R${salario_bruto - (IR + INSS)}'))
elif salario_bruto > 2500:
    IR = salario_bruto * 0.2
    INSS = salario_bruto * 0.12
    FGTS = salario_bruto * 0.11
    print(print(f'Salário Bruto:         R${salario_bruto}'
                f'\n(-)IR(10%) :           R${IR}'
                f'\n(-)INSS(10%)           R${INSS}'
                f'\n( )FGTS(11%)           R${FGTS}'
                f'\n   Total de descontos  R${IR + INSS}'
                f'\n   Salário Líquido     R${salario_bruto - (IR + INSS)}'))
