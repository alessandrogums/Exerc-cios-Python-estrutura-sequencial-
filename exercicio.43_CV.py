#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida

sexo=str(input(' digite a inicial do seu sexo, sendo H para homem e M para mulher: ')).strip()
if sexo=='M':
    print(' voce é mulher')
    altura=float(input('agora digite sua altura'))
    peso=float(input('agora digite seu peso '))
    imc=peso/((altura)**2)
    if imc < 18.5:
        print('você está abaixo do peso')
    elif 25>imc>18.5:
        print(' você está no seu peso ideal')
    elif 30>imc>25:
        print(' você está acima do peso, no caso como sobrepeso')
    elif 40>imc>30:
        print(' você está obesa')
    elif imc> 40:
        print(' você está em obesidade Mórbida')
elif sexo=='H':
    print('você é homem')
    altura = float(input('agora digite sua altura'))
    peso = float(input('agora digite seu peso '))
    imc = peso / ((altura) ** 2)
    if imc < 18.5:
        print('você está abaixo do peso')
    elif 25 > imc > 18.5:
        print(' você está no seu peso ideal')
    elif 30 > imc > 25:
        print(' você está acima do peso, no caso como sobrepeso')
    elif 40 > imc > 30:
        print(' você está obeso')
    elif imc > 40:
        print(' você está em obesidade Mórbida')
else:
    print('você não digitou corretamente')
