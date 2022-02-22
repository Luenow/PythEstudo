from random import choice
a1 = input('Primeiro Aluno: ')
a2 = input('Segundo Aluno: ')
a3 = input('Terceiro Aluno: ')
a4 = input('Quarto Aluno: ')
lista = [a1, a2, a3, a4]
sortear = choice(lista)
print('O aluno escolhido foi {}'.format(sortear))

'''random.choices(population, weights=None, *, cum_weights=None, k=1)
Retorna uma lista do tamanho de k de elementos escolhidos da population com substituição. Se a population estiver vazio,
levanta IndexError.

Se uma sequência weights for especificada, as seleções serão feitas de acordo com os pesos relativos.
 Alternativamente, se uma sequência cum_weights for fornecida, as seleções serão feitas de acordo com os pesos cumulativos
(talvez calculados usando itertools.accumulate()). Por exemplo, os pesos relativos [10, 5, 30, 5] são equivalentes aos pesos cumulativos [10, 15, 45, 50].
Internamente, os pesos relativos são convertidos em pesos acumulados antes de fazer seleções, portanto, fornecer pesos cumulativos economiza trabalho.

Se nem weights nem cum_weights forem especificados, as seleções serão feitas com igual probabilidade.
Se uma sequência de pesos for fornecida, ela deverá ter o mesmo comprimento que a sequência population.
É um TypeError para especificar ambos os weights e cum_weights.

weights ou cum_weights pode usar qualquer tipo numérico que interopera com os valores float retornados por random() 
(que inclui inteiros, ponto flutuantes, e frações mas exclui decimais). Assume-se que pesos serão não-negativos e finitos. Uma ValueError é levantada se todos os pesos forem zero.

Para uma dada semente, a função choices() com igual peso normalmente produz uma sequência diferente das chamadas repetidas para choice(). 
O algoritmo usado por choice() usa aritmética de ponto flutuante para consistência e velocidade internas.
O algoritmo usado por choice() assume como padrão aritmética inteira com seleções repetidas para evitar pequenos vieses de erro de arredondamento.'''