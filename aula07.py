# Classe: Modelo ou estrutura que define um objeto
# Objeto: Uma instância de uma classe
# Atributo: variaveis
# Métodos: Funções
class Animal:
    def __init__(self,nome):
        self.nome = nome
    def som(self):
        print(f"{self.nome} faz:")
class Gato(Animal):
    def som(self):
        print(f"O gato {self.nome} faz Miau")
class Dog(Animal):
    def som(self):
        print(f"O cachorro {self.nome} diz: AuAuAu!")
# gato1 = Gato("Tom")
# gato1.som()
# dog1 = Dog("Rex")
# dog1.som()
animais = [Dog("Rex"), Gato("Tom")]
for animal in animais:
    animal.som()
# a.latir()
# class ContaBancaria:
#     def __init__(self, titular, saldo):
#         self.titular = titular
#         self.__saldo = saldo
#     def versaldo(self):
#         return self.__saldo
#     def depositar(self,valor):
#         if valor > 0:
#             self.__saldo += valor
# c1 = ContaBancaria("Maria", 100.00)
# print(c1.versaldo())
# c1.depositar(130)
# print(c1.versaldo())

    
   