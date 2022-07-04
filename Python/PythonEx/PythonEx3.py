"""Exercício"""
"""Faça um programa que leia dois números e exiba o maior deles."""

numero1 = int(input("Digite o primeiro número qualquer: "))
numero2 = int(input("Digite o segundo número qualquer: "))

if numero1 > numero2:
    print("{} é maior que {}".format(numero1, numero2))
else:
    print("{} é maior que {}".format(numero2, numero1))