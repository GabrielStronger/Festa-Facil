#DUPLA: GABRIEL TORRES /  YASMIN BRAGA                          



                                #JUSTIFICATIVA

# Estrutura de dados a seer usada é fila, é como uma linha de espera onde as tarefas entram em uma 
#ordem e são realizadas uma de cada vez,na ordem em que chegaram. Isso significa que a primeira
#tarefa a entrar é a primeira a ser concluída. 
#Assim, as subtarefas são feitas uma a uma e quando uma tarefa termina, a próxima começa. 
#Isso garante que tudo seja feito na ordem certa.

                               #PROPOSTA DE IPLEMENTAÇÃO:
#UMA EMPRESA QUE ORGANIZA FESTAS; 
# A tarefa principal é organizar uma festa, e as substarefas são os atos
# feitos para que a festa esteja organizada de fato, como fazer o bolo, eviar convites, montar mesas etc..

# Classe que mostra codigo proposta de implementação.
from collections import deque

class Tarefa:
    def __init__(self, nome, subtarefas):
        self.nome = nome
        self.subtarefas = deque(subtarefas)  # Usando deque para as subtarefas
    
    # Jeito usado para processar cada subtarefa
    def processar_subtarefas(self):
        while self.subtarefas:
            subtarefa = self.subtarefas.popleft()  # Retira a subtarefa da fila
            print(f"Processando subtarefa: {subtarefa}")
        print(f"Tarefa '{self.nome}' concluída!\n")

# Classe para manipular o sistema de tarefas
class SistemaDeTarefas:
    def __init__(self):
        self.fila_de_tarefas = deque()  # Usando deque para a fila de tarefas
    
    # Coloca uma tarefa à fila
    def adicionar_tarefa(self, tarefa):
        self.fila_de_tarefas.append(tarefa)
    
    # Processa todas as tarefas na fila
    def processar_tarefas(self):
        while self.fila_de_tarefas:
            tarefa_atual = self.fila_de_tarefas.popleft()  # Tira a tarefa da fila
            tarefa_atual.processar_subtarefas()

# Criando tarefas com subtarefas
tarefa1 = Tarefa("Comprar ingredientes", ["Comprar farinha", "Comprar ovos", "Comprar leite"])
tarefa2 = Tarefa("Preparar bolo", ["Misturar ingredientes", "Assar o bolo" , "Decorar o bolo"])
tarefa3 = Tarefa("Organizar festa", ["Enviar convites", "Decorar a sala", "Montar a mesa", "Preparar música"])

# Criando o sistema de tarefas
sistema = SistemaDeTarefas()

# Colocando as tarefas ao sistema
sistema.adicionar_tarefa(tarefa1)
sistema.adicionar_tarefa(tarefa2)
sistema.adicionar_tarefa(tarefa3)

# Processando todas as tarefas
sistema.processar_tarefas()
