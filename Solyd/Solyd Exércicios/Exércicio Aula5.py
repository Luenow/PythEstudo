'''EXERCICIO: Faça um programa que leia a quantidade de pessoas que
serao convidadas para uma festa.
Após isso o programa irá perguntar o nome de todas as pessoas e colocar numa lista de convidados
Após isso irá imprimir todos os nomes da lista
'''
print('Programa de controle de festinha 1.0')
print('#' * 35)

quantidade = input('Quantidade de pessoas: ')
lista_de_convidados = []


i = 1

while i <= int(quantidade):
    nome_do_convidado = input('Digite seu nome de convidado: #'+ str(i) +': ')
    lista_de_convidados.append(nome_do_convidado)
    i += 1

print('Serão', quantidade, 'convidados')
print('\nLISTA DE CONVIDADOS')

for convidado in lista_de_convidados:
    print(convidado)




