#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros

print('-'*40,'Loja de produtos','-'*40)
produtos=float(input('digite o valor do(s) produto(s)'))
opcoes=int(input('voce terá 4 opções de pagamento: '
                 '\n1)à vista no dinheiro/cheque (10% de desconto)'
                 '\n2)à vista no cartão (5% de desconto) '
                 '\n3)2vezes no cartão(preço normal) '
                 '\n4)3 vezes ou mais no cartão(20% de juros)'
                 '\nescolha uma delas : '))
if opcoes==1:
    pagamento=0.9*produtos
    print(f'você irá pagar R${pagamento:.2f} , devido aos 10% de desconto')
elif opcoes==2:
    pagamento=0.95*produtos
    print(f'você irá pagar R${pagamento:.2f} , devido aos 5% de desconto')
elif opcoes==3:
    print(f'então você pagara o valor real do(s) produto(s), que é de R${produtos},com as parcelas de  R${produtos/2}')
elif opcoes==4:
    produto_juros=1.2*produtos
    numero_parcelas=int(input('digite o numero de parcelas(3 vezes ou mais):'))
    if numero_parcelas>=3:
        valor_parcelas = produto_juros /numero_parcelas
        print(f'voce pagará no total R$ {produto_juros:.2f}, com parcelas no valor de R$ {valor_parcelas:.2f}')
    else:
        print('você digitou errado!')
else:
    print('digitaste errado!!!')
