'''
Exercício 01

Preencha um dicionário com as informações de 5 produtos.
Utilize o nome do produto como chave e o preço como valor. 
Solicite os dados ao usuário.
Percorra o dicionário e exiba o nome dos produtos com preço superior a R$ 50.00

Exemplo:
Veja um exemplo da estrutura do dicionário.
{'Caneta': 3.0, 'Pen Drive': 100.0, 'Teclado': 30.0, 'Lápis': 1.50}
_________________________________________________________________________
'''
# produtos = {'Caneta': 3.0, 'Pen Drive': 100.0, 'Teclado': 30.0, 'Lápis': 1.50, 'Notebook': 4999.99}

# while True:
#     nome = input('Produto: ')
#     if nome == '':
#         break
#     preco = float(input('Preço do produto: '))
#     if nome in produtos:
#         print('Produto já cadastrado!')
#     else:
#         produtos[nome] = preco    
#         for x in produtos:
#             if produtos[x] >= 50:
#                 print(x, produtos[x])
'''
Exercício 02

Preencha um dicionário com os dados de 5 alunos.
Utilize o ra do aluno como chave e uma lista de três notas como valor.
Percorra o dicionário e exiba a média de cada aluno.

Exemplo:
Veja um exemplo da estrutura do dicionário.
{1901502: [10, 8, 7.5], 2002441: [6, 5, 7.5], 2001332: [5, 8, 9.5]}

_________________________________________________________________________
'''
# alunos_notas = {1901502: [10, 8, 10], 2002441: [6, 5, 7.5], 2001332: [9, 8, 9], 2002500: [6, 8, 8], 2001222: [6, 8, 10] }

# for ra in alunos_notas:
#   media = sum(alunos_notas[ra]) / len(alunos_notas[ra])       
#   print(f'O aluno {ra}, ficou com a média de notas: {media:.2f}.')

'''
Exercício 03

Escreva uma função que conta a quantidade de vogais em um texto e armazena tal quantidade em um dicionário, onde a chave é a vogal considerada e o valor é a quantidade de vezes que essa vogal aparece no texto. 
A função deve receber o texto como entrada, e retornar o dicionário.

Exemplo:
Para o texto abaixo:
'faculdade de tecnologia impacta'
A função deve retornar o seguinte dicionário:
{'a': 5, 'u': 1, 'e': 3, 'o': 2, 'i': 2}


# exemplo de como percorrer uma string
texto = 'faculdade de tecnologia impacta'
for c in texto:
  if c == ‘a’:
'''
# def contador_de_caracteres():
#   import re      
#   texto = 'faculdade de tecnologia impacta'
#   a = len(re.findall('a', texto))
#   e = len(re.findall('e', texto))
#   i = len(re.findall('i', texto))
#   o = len(re.findall('o', texto))
#   u = len(re.findall('u', texto))
#   resultado = {'a': a, 'e': e, 'i': i, 'o': o, 'u': u}
#   print(resultado)  
      
# if __name__ == '__main__':
#   contador_de_caracteres()


