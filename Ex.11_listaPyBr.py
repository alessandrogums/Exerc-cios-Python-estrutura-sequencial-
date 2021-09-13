
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

salario_inicial=float(input('digite seu salário R$:'))
opcoes=' '
while True:
    opcoes=int(input('digite qual opção você quer saber?'
                 '\n[1]o Salário antes do ajuste'
                 '\n[2]o percentual de aumento aplicado '
                 '\n[3]o valor do aumento'
                 '\n[4]o novo salário, após o aumento'
                 '\n[5]Sair da consulta '
                '\n escolha:'))
    if opcoes==1:
        print(f'seu salário antes do ajuste é:{salario_inicial}')
        escolha=int(input('quer continuar?[1] para sim e [2]não:'))
        if escolha==2:
            break
        else:
            print('voltando ao menu....')
    if opcoes==2:
        if salario_inicial<280:
            print('o aumento foi de 20%')
        elif 700>salario_inicial>280:
            print('o aumento foi de 10%')
        elif 1500>salario_inicial>700:
            print('o aumento foi de 10%')
        elif salario_inicial>1500:
            print('o aumento foi de 5%')
        escolha = int(input('quer continuar?[1] para sim e [2]não:'))
        if escolha == 2:
            break
        else:
            print('voltando ao menu....')
    if opcoes==3:
        if salario_inicial<280:
            print(f'o aumento foi de  R${salario_inicial*0.2}')
        elif 700>salario_inicial>280:
            print(f'o aumento foi de R${salario_inicial*0.15}')
        elif 1500>salario_inicial>700:
            print(f'o aumento foi de R${salario_inicial*0.1}')
        elif salario_inicial>1500:
            print(f'o aumento foi de R${salario_inicial*0.05}')
        escolha = int(input('quer continuar?[1] para sim e [2]não:'))
        if escolha == 2:
            break
        else:
            print('voltando ao menu....')
    if opcoes==4:
        if salario_inicial<280:
            print(f'o salario após o aumento fica de R$:{salario_inicial*1.2}')
        elif 700>salario_inicial>280:
            print(f'o salário após o aumento fica de R$:{salario_inicial*1.15}')
        elif 1500>salario_inicial>700:
            print(f'o salário após o aumento fica de R$:{salario_inicial*1.1}')
        elif salario_inicial>1500:
            print(f'o salário após o aumento fica de R$:{salario_inicial*1.05}')
        escolha = int(input('quer continuar?[1] para sim e [2]não:'))
        if escolha == 2:
            break
        else:
            print('voltando ao menu....')
    if opcoes==5:
        print('saindo do menu...')
        break
