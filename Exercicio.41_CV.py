#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER

import datetime
ano_nasc=int(input(' digite o ano de nascimento'))
ano_atual=datetime.date.today().year
idade=ano_atual- ano_nasc
print(f'ahh, você tem :{idade} anos então')
if idade<=9:
    print('sua classificação é mirim')
elif 14>=idade>9:
    print('sua classificação é infantil')
elif 19>=idade>14:
    print(' sua classificação é junior')
elif 25>=idade>19:
    print(' sua classificação é senior')
else :
    print(' sua classificação é master')

print('='*30,'FINAL DO PROGRAMA','='*40)
