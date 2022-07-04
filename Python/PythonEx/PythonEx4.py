"""Exercício"""
"""Faça um programa que leia a altura de uma pessoa que irá entrar num brinquedo de um parque de diversões.
Se a altura do usuário for acima de 1.61. Escrever que ele pode entrar no brinquedo, senão, escrever que ele não pode brincar."""

altura = float(input("Me diz qual é sua altura: "))

if altura > 1.61:
    print("Você pode entrar no brinquedo")
else:
    print("Não está de acordo com sua altura para usar o brinquedo")