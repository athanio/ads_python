import datetime
# a , b, c = map(float, input('Digite 3 valores').split())

# nome = "IFPI"
# y = "2024 "
# y += nome  # y = y + nome
# a = a + 1  # a += 1

# print("Valor de a = " ,a)
# print(y)

# if a == 3 and b == 2:
#     print("valor igual a 3")
#     print('letras')

# vetor = [2, 4, 8]
# print(vetor)
# resultado = list(map(lambda x: x ** 2, vetor))

# print(resultado)

# print(f"Valor a: {a} ")
# print("Valor b: ", b)
# print("Valor c: ", c)
v1 = [3, 2 , 7, 4 , 5]
def quadrado(x):
    a = 0
    if x % 2 == 0:
        a = x
    return a

v2 = list(map(quadrado, v1 ))
print(v2)
print()