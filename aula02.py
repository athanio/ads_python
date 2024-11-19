#aula string
a = "TESTE"
b = "aula"

a = a[2]

c = b.upper()
d = a.lower()
mensagem = a + b
print(mensagem)

nome = " ifpi parnaiba "
novo = nome.replace('parnaiba','Teresina')

print(novo)

nome = nome.strip()
n = len(nome)
texto = "Maça, Banana, Laranja, Manga"
frutas = texto.split(", ")
print(frutas)

carros = ['fiat','toyota','volks','ford']
dados = " : ".join(carros)

print(carros)
print(dados)

pesquisa = "ford" in dados
if pesquisa :
    print("Localizado")
else:
    print("Nao encontrado")
    
nome1 = "Joaquim"
idade = 20
msn1 = "Meu nome {} \n minha \"idade\" {}".format(nome1,idade)
msn2 = f"Meu nome {nome1} \n minha \"idade\" {idade}"

print(msn1)
print(msn2)


print(n)
print(c)
print(d)

### Exercícios

#1. Crie uma string que contenha seu nome e sua profissão. 
# Em seguida, concatene essa string com uma saudação.

#2. Peça ao usuário para inserir uma frase e conte 
# quantas vezes uma letra específica aparece na frase usando o método `.count()`.

#3. Dada uma lista de frutas, converta-a em uma string 
# separada por vírgulas e espaços.