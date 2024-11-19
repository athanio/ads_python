a = 10
minha_lista = [1,2,4,6,8]

minha_lista.append(5)
minha_lista.insert(2,9)
minha_lista.pop(4)
print(minha_lista)

#tuplas

lista = [1,2,3,'a']
tuplas = ('a','b','c')
dicionario = { }
minha_lista = list(tuplas)
m_tuplas = tuple(lista)
print(minha_lista)
print(m_tuplas)

numeros = [1,2,8,4,5]
for x in numeros:
    print(x)
quadrados = [x * 3 for x in numeros if x % 2 == 0]
print(quadrados)
# 1 Dada uma lista de strings, crie uma nova lista contendo apenas as palavras que possuem todas 
# as suas letras em maiúsculo e que têm um comprimento maior que 4.

# Entrada: ['PYTHON', 'java', 'JAVASCRIPT', 'C', 'RUBY']
# Saída: ['PYTHON', 'JAVASCRIPT']

# 2 Dada uma tupla contendo pares de números, retorne a soma de todos os segundos elementos de cada par.
# Entrada: ((1, 2), (3, 4), (5, 6))
# Saída: 12 (2 + 4 + 6)