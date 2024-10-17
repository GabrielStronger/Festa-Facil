# 🎉 Festa Fácil - Simulação de Empresa Organizadora de Festas 🎉

## Descrição

*Festa Fácil* é um programa simples desenvolvido em Python que simula uma empresa organizadora de festas. A aplicação utiliza uma *fila* para gerenciar e processar diversas tarefas, cada uma contendo um conjunto de subtarefas. As tarefas são realizadas em ordem de chegada, garantindo que tudo seja executado de forma organizada e eficiente.

O sistema foi pensado para automatizar atividades comuns no processo de preparação de uma festa, como a compra de ingredientes, a preparação de um bolo, e a organização do evento.

## Como o Programa Funciona

1. *Tarefas*: Cada tarefa representa uma atividade a ser realizada para organizar uma festa. Exemplos de tarefas incluem "Comprar ingredientes", "Preparar bolo" e "Organizar festa".
   
2. *Subtarefas*: Cada tarefa é composta por diversas subtarefas. Por exemplo, a tarefa "Comprar ingredientes" pode conter as subtarefas "Comprar farinha", "Comprar ovos" e "Comprar leite".

3. *Fila de Tarefas*: As tarefas são organizadas em uma fila (estrutura de dados FIFO - First In, First Out). Isso garante que as tarefas sejam processadas na ordem em que foram adicionadas.

4. *Processamento*: O sistema processa cada subtarefa de uma tarefa antes de passar para a próxima. Quando todas as subtarefas de uma tarefa são concluídas, a próxima tarefa na fila é iniciada.

## Exemplo

Suponha que a empresa tenha três tarefas a serem realizadas:

- *Tarefa 1: Comprar ingredientes*
  - Subtarefas: "Comprar farinha", "Comprar ovos", "Comprar leite"

- *Tarefa 2: Preparar bolo*
  - Subtarefas: "Misturar ingredientes", "Assar o bolo", "Decorar o bolo"

- *Tarefa 3: Organizar festa*
  - Subtarefas: "Enviar convites", "Decorar a sala", "Montar a mesa", "Preparar música"

O programa processará todas essas tarefas na ordem em que foram adicionadas, garantindo que cada subtarefa seja concluída antes de passar para a próxima.

## Como Executar

### Pré-requisitos

- Ter o Python 3.x instalado no sistema.
- Um terminal ou prompt de comando.

### Passos

1. Clone este repositório na sua máquina local:

   ```bash
   git clone https://github.com/GabrielSronger/festa-facil.git
