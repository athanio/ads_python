import json
dic = { 
    "nome": "Maria",
    "idade": 25,
    "cidade": "phb"
}
dados = '{"nome": "joao", "idade": 13, "habilidade": [ "php", "py", "js"],"cidade": "Parnaiba"}' 
jsondados = json.loads(dados)

print(jsondados['cidade'])
print(jsondados['idade'])
print(jsondados['habilidade'][1])

with open("nome_arquivo.json", "w") as arquivo:
    dados = json.dump(dados, arquivo)

with open('nome_arquivo.json', 'r') as arquivo:
    leitura = json.load(arquivo)
print (leitura)


