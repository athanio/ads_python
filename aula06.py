#arquivo abertura
a =  10
arquivo = open('exemplo.txt',"a") 
arquivo.write(f" \n Parnaiba 04 {a}")
#arquivo Leitura

# with open("exemplo.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

nomes = ['Aline\n', 'Maria\n', 'João\n']
with open('nomes.txt', "w") as arquivo:
      arquivo.writelines(nomes)

with open('nomes.txt', "r") as arquivo:
      print(" --- Nomes da Agenda -- ")
      for linha in arquivo:
            print(linha.strip())

import csv
with open('alunos.csv', "w", newline='') as csvfile:
      escreva = csv.writer(csvfile)
      escreva.writerow(['Nome', 'Nota'])

with open('alunos.csv', 'r') as csvfile:
      reader = csv.reader(csvfile)
      for linha in reader:
            print(linha)

import json    
dados = {'nome':'João', 'idade': 23, 'cidade':'Parnaiba'}
with open('dados.json', "w") as jsonfile:
      json.dump(dados, jsonfile)

with open('dados.json', 'r') as jsonfile:
      dados = json.load(jsonfile)
      print(dados) 






