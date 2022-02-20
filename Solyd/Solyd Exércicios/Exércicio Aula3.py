'''
EXERCICIO:
Faça um programa que pergunte a idade, o peso e a altura de uma
pessoa e decide se ela esta apta a ser do Exercito
Para entrar no exercito é preciso ter mais de 18 anos pesar mais ou igual 60 kilos
e medir mais ou igual 1,70 metros
'''

idade = int(input('Qual a sua idade? '))
peso = int(input('Quanto você pesa? '))
altura = float(input('Você mede quantos de altura? '))

if (idade >= 18) and (peso >= 60) and (altura >= 1.70):
    print('Você está classificado para entrar no exercito.')
else:
    print('Você não está classificado para entrar no exercito!')