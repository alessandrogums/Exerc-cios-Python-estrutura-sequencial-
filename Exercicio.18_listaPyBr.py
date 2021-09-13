#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia = int(input('digite algum dia do ano:'))
mes = str(input('digite algum mês do ano:')).strip()
ano = int(input('digite um ano qualquer:'))
data = (f'{dia}/{mes}/{ano}')

if mes>12 or mes<1:
    print(f'a data {data} não existe!')
elif dia>31 or dia<1:
    print(f'a data{data} não existe!')
if mes in '04,06,09' or mes == '11':
    if dia != 31 and dia > 0:
        print(f'a data {data} existe!')
    else:
        print(f'infelizmente a data {data} não existe')
elif mes == '02':
    if (ano % 4 == 0  and ano % 100 != 0) or ano % 400 == 0:
        if 0 < dia <= 29:
            print(f'a data {data} existe!')
        else:
            print(f'a data {data} não existe')
    else:
        if 0 < dia <= 28:
            print(f'a data {data} existe!')
        else:
            print(f'a data {data} não existe')
