#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
#entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

print('olá, estamos fazendo uma investigação. Peço que me responda algumas perguntas com sim ou não: ')
pergunta_1=str(input('Você telefonou para a vítima?')).strip().lower()[0]
pergunta_2=str(input('Esteve no local do crime?')).strip().lower()[0]
pergunta_3=str(input('Mora perto da vítima?')).strip().lower()[0]
pergunta_4=str(input('Devia para a vítima?')).strip().lower()[0]
pergunta_5=str(input('Já trabalhou com a vítima?')).strip().lower()[0]
lista=[pergunta_1,pergunta_2,pergunta_3,pergunta_4,pergunta_5]
qte_sim=lista.count('s')
qte_nao=lista.count('n')
if qte_sim==2:
    print('você é suspeito..')
elif qte_sim==3 or qte_sim==4:
    print('você participou do assassinato. Deve ter sido cumplice')
elif qte_nao==0:
    print('meu deus. Você é o assassino.Está preso em nome da lei!')
