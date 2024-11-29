import random
import datetime
import math

# Lista de tarefas
tarefas = [
    "Ler um capítulo de livro", 
    "Fazer exercício físico", 
    "Estudar um novo tópico", 
    "Cozinhar uma refeição", 
    "Meditar por 30 minutos", 
    "Organizar a casa", 
    "Assistir a um documentário"
]

# Função para gerar um tempo de execução aleatório (em minutos) entre 20 e 90 minutos
def gerar_tempo_aleatorio():
    return random.randint(20, 90)

# Função para registrar o tempo de execução de cada tarefa
def registrar_tarefa(tarefa):
    tempo_inicial = datetime.datetime.now()
    print(f"Iniciando a tarefa: '{tarefa}' em {tempo_inicial.strftime('%H:%M:%S')}")
    
    # Gerando um tempo aleatório de execução para a tarefa
    tempo_execucao = gerar_tempo_aleatorio()
    # Simulando o tempo de execução (dormindo o processo por 'tempo_execucao' segundos)
    print(f"Tempo estimado: {tempo_execucao} minutos...")
    
    # Esperar o tempo de execução simulado
    datetime.datetime.now() + datetime.timedelta(minutes=tempo_execucao)
    
    tempo_final = datetime.datetime.now()
    print(f"Tarefa '{tarefa}' concluída em {tempo_final.strftime('%H:%M:%S')}")
    
    # Calculando a diferença de tempo
    tempo_duracao = (tempo_final - tempo_inicial).total_seconds() / 60  # duração em minutos
    return tempo_duracao

# Função para gerar um relatório das tarefas
def gerar_relatorio(tarefas_realizadas):
    tempos = [tarefa['tempo'] for tarefa in tarefas_realizadas]
    tempo_total = sum(tempos)
    
    # Calculando as estatísticas
    tempo_medio = math.fsum(tempos) / len(tempos)
    tempo_minimo = min(tempos)
    tempo_maximo = max(tempos)
    
    # Exibindo o relatório
    print("\nRelatório semanal:")
    print(f"Tempo total gasto em tarefas: {tempo_total:.2f} minutos")
    print(f"Tempo médio por tarefa: {tempo_medio:.2f} minutos")
    print(f"Tempo mínimo por tarefa: {tempo_minimo:.2f} minutos")
    print(f"Tempo máximo por tarefa: {tempo_maximo:.2f} minutos")
    
    # Cálculo da desvio padrão dos tempos
    desvio_padrao = math.sqrt(sum((x - tempo_medio) ** 2 for x in tempos) / len(tempos))
    print(f"Desvio padrão do tempo gasto: {desvio_padrao:.2f} minutos")

# Função principal para rodar o programa
def main():
    tarefas_realizadas = []
    
    # Gerando tarefas para 7 dias da semana
    for dia in range(1, 8):  # Para cada dia da semana
        tarefa_do_dia = random.choice(tarefas)
        tempo_duracao = registrar_tarefa(tarefa_do_dia)
        
        # Armazenando a tarefa e seu tempo de execução
        tarefas_realizadas.append({
            'dia': dia,
            'tarefa': tarefa_do_dia,
            'tempo': tempo_duracao
        })
        
        print("-" * 30)
    
    # Gerando relatório após todas as tarefas
    gerar_relatorio(tarefas_realizadas)

# Executando a função principal
if __name__ == "__main__":
    main()
