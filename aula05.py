#Dicionário
alunos = {
    "1" : {    
     "nome": "João",
     "idade": 20,
     "curso": "Engenharia"
    },
    '2': {
     "nome" : "Maria",
     "idade": 22,
     "curso": "Engenharia"
    }
}
alunos['1']['curso'] = "Informática"
# for x, y in alunos.items():
#     print(f"Dados do dicionario { x } e o valor {y['nome']}")
for x in alunos:
    print(alunos[x]['idade'])