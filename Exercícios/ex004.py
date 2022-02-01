algo = input('Digite um algo: ')
print('O tipo primitivo desse valor é', type(algo))
print('Só tem espaços?', algo.isspace()) #Se tem espaços
print('É um número? ', algo.isnumeric()) #Se tem número
print('É alfabético?', algo.isalpha()) #Se tem só letras
print('É alfanumérico', algo.isalnum()) #Se tem só número
print('Está em maiúsculas?', algo.isupper()) #Se tudo está maiúsculo
print('Está em minúsculas?', algo.islower()) #Se tudo está minúsculo
print('Está capitalizada?', algo.istitle())