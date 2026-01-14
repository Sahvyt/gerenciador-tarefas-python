# Gerenciador de Tarefas em Python (CLI)

Aplicação simples de linha de comando desenvolvida em Python para gerenciar tarefas, permitindo adicionar, listar e concluir tarefas com persistência em arquivo JSON.

Este projeto foi criado com foco em praticar lógica de programação, manipulação de arquivos e organização de código em Python.

---

## Funcionalidades

- Adicionar novas tarefas
- Listar tarefas com status (pendente ou concluída)
- Marcar tarefas como concluídas
- Remover tarefas
- Editar tarefas
- Persistência de dados em arquivo JSON
- Interface simples via terminal (CLI)

---

## Estrutura do projeto

```text
gerenciador-tarefas-python/
├── .gitignore
├── main.py
├── tarefas.json  # Criado automaticamente ao executar
└── README.md
```

---

## Como executar

### Pré-requisitos
- Python 3.10 ou superior

### Passos
1. Clone o repositório ou faça o download dos arquivos
2. Navegue até a pasta do projeto
3. Execute o programa:

```bash
python main.py
```

4. Utilize o menu no terminal para gerenciar suas tarefas

---

## Exemplos de uso

```text
1 - Adicionar tarefa
2 - Listar tarefas
3 - Concluir tarefa
4 - Remover terefa
5 - Editar tarefa
0 - Sair
```

As tarefas são salvas automaticamente no arquivo tarefas.json.

---

## O que aprendi com esse projeto

- Leitura e escrita de arquivos JSON em Python
- Persistência de dados em aplicações simples
- Organização de um programa em funções
- Validação de entrada do usuário
- Uso de estruturas de dados como listas e dicionários
- Controle de fluxo em aplicações CLI
- Uso de `match/case` como alternativa moderna a `if/elif/else`
- Workflow profissional com Git (branches, commits, pull requests)

---

## Possíveis melhorias futuras

- Filtrar tarefas por status
- Interface gráfica ou versão web

---

## Autor

**Kauan Melo**
[GitHub](https://github.com/Sahvyt)
[LinkedIn](https://www.linkedin.com/in/kauan-melo-8b72a0305/)
