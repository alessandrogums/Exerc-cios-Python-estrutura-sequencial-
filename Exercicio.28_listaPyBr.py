#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. 
#Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
#Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
#contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

qte_carne = 0
preco_carne = 0
preco_kg = 0
print('=' * 70)
print('promoção supermercado Tabajara          Até 5 kg        Acima de 5kg'
      '\nFilé Duplo                            R$4,90 por kg    R$5,80 por kg'
      '\nalcatra                               R$5,90 por kg    R$6,80 por kg'
      '\nPicanha                               R$6,90 por kg    R$7,80 por kg')
print('=' * 70)
tipo_carne = str(input('escolha SOMENTE um tipo de carne, digitando sua primeira letra:')).strip().lower()[0]
while not tipo_carne in 'f,a,p':
    print('digitou errado!')
    tipo_carne = str(input(
        'digite APENAS a letra inicial referente a somente o único tipo de carne que você vai querer levar:')).strip().lower()[0]
if tipo_carne == 'f':
    tipo_carne = 'filé Duplo'
    qte_carne = int(input('digite quantos Kg de Filé Duplo você vai querer:'))
    if qte_carne <= 5:
        preco_kg = 4.9
        preco_carne = qte_carne * 4.9
    else:
        preco_kg = 5.8
        preco_carne = qte_carne * 5.8
elif tipo_carne == 'a':
    tipo_carne = 'alcatra'
    qte_carne = int(input('digite quantos Kg de Alcatra você vai querer:'))
    if qte_carne <= 5:
        preco_kg = 5.9
        preco_carne = qte_carne * 5.9
    else:
        preco_kg = 6.8
        preco_carne = qte_carne * 6.8
elif tipo_carne == 'p':
    tipo_carne = 'picanha'
    qte_carne = int(input('digite quantos Kg de Picanha você vai querer:'))
    if qte_carne <= 5:
        preco_kg = 6.9
        preco_carne = qte_carne * 6.9
    else:
        preco_kg = 7.8
        preco_carne = qte_carne * 7.8
pagamento = int(input('Por fim, qual seria a forma de pagamento?'
                      '\n[1]Cartão da nossa loja, tendo assim 5% de desc. sobre o total da compra'
                      '\n[2]pagamento à vista'
                      '\nopção>>'))
if pagamento == 1:
    print('                         NOTA FISCAL'
          f'\nForam escolhidos {qte_carne}Kg de {tipo_carne}'
          f'\no preço do Kg de {tipo_carne} foi R${preco_kg}'
          f'\no total era pra ser de R${preco_carne}'
          f'\nContudo, houve desconto de R${preco_carne * 0.05:.2f}, resultando em um preço final de R${preco_carne * 0.95:.2f} ')
else:
    print('                         NOTA FISCAL'
          f'\nForam escolhidos {qte_carne}Kg de {tipo_carne}'
          f'\no preço do Kg de {tipo_carne} foi R${preco_kg}'
          f'\no total foi de R${preco_carne:.2f}')
