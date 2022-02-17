'''
_________________________________________________________________________
 Exercício 01
 Preencha uma lista com 10 números digitados pelo usuário e exiba:
 a) o maior número da lista
 b) o menor número da lista
 c) a quantidade de números pares contidos na lista
 d) a média dos números contidos na lista
 e) todos os números menores do que a média calculada no item anterior
 _________________________________________________________________________
'''

# lista = []
# for i in range(10):
#     n = int(input("Número: "))
#     lista.append(n)
# maior = max(lista)
# menor = min(lista)
# media = sum(lista) / len(lista)
# print(f'O maior número da lista é: {maior}')
# print(f'O menor número da lista é: {menor}')
# print(f'A média dos números contidos na lista é: {media}')
# menor_media = sorted(filter(lambda x: x < media, lista))
# print(f'Os números na lista menores que a média são: {menor_media}')

# numero_par = 0
# for num in lista:
#     if num % 2 == 0:
#         numero_par += 1
# print(f'Essa lista possui {numero_par} números pares.')

'''
_________________________________________________________________________
Exercício 02
Preencha uma lista com 10 números digitados pelo usuário. A partir desta lista, gere uma lista com
os números pares e outra com os números ímpares.
Exemplo:
Suponha que a lista digitada seja: [1, 4, 7, 9, 5, 3, 7, 9, 8, 8].
Para esta lista, o programa deve gerar as seguintes listas:
[4, 8, 8]
[1, 7, 9, 5, 3, 7, 9]
_________________________________________________________________________
'''

# lista = []
# lista_par = []
# lista_impar = []

# for i in range(10):
#     n = int(input("Número: "))
#     lista.append(n)
# lista_par = sorted(filter(lambda x: x % 2 == 0, lista))
# lista_impar = sorted(filter(lambda x: x % 2 != 0, lista))
# print(f'Lista de números pares: {lista_par}')
# print(f'Lista de números ímpares: {lista_impar}')

'''
_________________________________________________________________________
Exercício 03
Preencha duas tuplas com 5 números cada, informados pelo usuário. Concatene as duas tuplas e
exiba a tupla resultante.
Dica: primeiro crie duas listas, e então, converta as listas em tuplas utilizando a função tuple.
tupla = tuple(lista) converte a lista em uma tupla
Exemplo: Suponha que as tuplas contenham os números:
(3, 1, 5, 3, 5)
(5, 5, 7, 3, 1).
Como resultado, o programa deve gerar a tupla:
(3, 1, 5, 3, 5, 5, 5, 7, 3, 1).
_________________________________________________________________________
'''

# lista_1 = [1, 2, 3, 4, 5]
# lista_2 = [6, 7, 8, 9, 10]
# tupla = tuple(lista_1) + tuple(lista_2)

# print(tupla)

'''
_________________________________________________________________________
Exercício 04
Escreva uma função chamada intercala_numeros que recebe como entrada duas listas de três
elementos e retorna uma lista de seis elementos, com os números intercalados.
Exemplo: Suponha que as listas de entrada da função sejam:
[1, 2, 3]
[4, 5, 6]
Para estas listas, a função deve retornar:
[1, 4, 2, 5, 3, 6]
_________________________________________________________________________
'''

# def intercala_numeros():
#     lista_1 = [1, 2, 3]
#     lista_2 = [4, 5, 6]
#     lista = []
#     for i in range(0 ,3):
#         lista.append(lista_1[i])
#         lista.append(lista_2[i])
#     return lista

# print(intercala_numeros())