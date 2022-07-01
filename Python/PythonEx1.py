'''Exercício'''
'''Faça um programa que leia 3 notas e calcula a média. E se a média for maior ou igual a 6,
escreva "Aprovado" senão, escreva "recuperação"'''


nota1 = float(input("Digite primeira nota: "))
nota2 = float(input("Digite segunda nota: "))
nota3 = float(input("Digite terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print("Sua média vai ser {}.".format(media))
if media >= 6 :
    print("Você foi aprovado")
else:
    print("Você está de recuperação!")