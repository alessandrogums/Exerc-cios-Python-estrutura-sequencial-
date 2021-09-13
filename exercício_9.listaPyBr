 #Faça um Programa que leia três números e mostre-os em ordem decrescente.
  a=b=c=0
 (a é o maior, b é o valor intermediário, c é o menor valor)
 for contador in range(1,4):
    num=float(input(f'digite o númeroº{contador}'))
     if contador==1:
         a=b=c=num
     if contador==2:
         if num>a:
            a=num
         else:
             b=num
     print(a,b,c)
     if contador==3:
         if num>a:
             c=b
             b=a
             a=num
         elif a>num>b:
             c=b
            b=num
         elif num<b:
             c=num

print(f' a ordem decrescente é :{a,b,c}' )
