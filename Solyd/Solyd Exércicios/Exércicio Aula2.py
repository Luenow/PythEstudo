'''
Exércicios: Faça um formulario que pergunte o nome, cpf, endereço, idade, altura e telefone
e imprima isso em um relatorio organizado
'''

nome = input('Qual é seu nome? ')
cpf = input('Digite seu CPF: ')
endereco = input('Onde você mora? ')
idade = input('Quantos anos você tem? ')
altura = input('Qual altura você mede? ')
telefone = input('Digite número de telefone: ')
print('=' * 10 )
print('Nome: {:2}\nCPF: {:2}\nEndereço: {:2}\nIdade: {:2}\nAltura: {:2}\nTelefone: {:2}'.format(nome, cpf, endereco, idade, altura, telefone))
print('=' * 10)
