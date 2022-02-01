a = int(input('Primeiro bimestre: '))
if a > 10:
    a = int(input('Você digitou errado. Primeiro Bimestre'))
b = int(input('Segundo bimestre:  '))
if b > 10:
    b = int(input('Você digitou errado. Segundo Bimestre'))
c = int(input('Terceiro bimestre:  '))
if c > 10:
    c = int(input('Você digitou errado. Terceiro Bimestre'))
d = int(input('Quarto bimestre:  '))
if d > 10:
    d = int(input('Você digitou errado. Quarto Bimestre'))
media = (a + b + c + d) / 4
if a < 10 and b < 10 and c < 10 and d < 10:
    print('media: {}'.format(media))
else:
    print('foi informado alguma nota errada')



#a = int(input('Entre com primeiro valor: '))
#b = int(input('Entre com segundo valor: '))
#resto_a = a % 2
#resto_b = b % 2
#if resto_a == 0 or not resto_b > 0:
#    print('foi digitado um numero é par')
#else:
#    print('nenhum numero é impar')


#a = input('Primeiro valor: ')
#b = input('Segundo valor: ')
#c = input('Terceiro valor: ')
#if a > b and a > c:
#    print('o maior número é {}'.format(a))
#elif b > a and b > c:
#    print('o maior número é {}'.format(b))
#else:
#    print('o maior número é {}'.format(c))w
#print('final do programa')