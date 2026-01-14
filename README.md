# Gerenciador de Tarefas em Python (CLI)

Aplicação simples de linha de comando desenvolvida em Python para gerenciar tarefas, permitindo adicionar, listar e concluir tarefas com persistência em arquivo JSON.

Este projeto foi criado com foco em praticar lógica de programação, manipulação de arquivos e organização de código em Python.

---

## Funcionalidades

- Adicionar novas tarefas
- Remover tarefas
- Marcar tarefas como concluídas
- Editar tarefas
- Listar tarefas com filtros por status:
  - Listar todas as tarefas
  - Listar somente tarefas concluídas
  - Listar somente tarefas pendentes
- Persistência de dados em arquivo JSON
- Interface simples via terminal (CLI) com menu hierárquico

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

### Menu Principal

```text
========================================
1 - Adicionar tarefa
2 - Remover tarefa
3 - Concluir tarefa
4 - Editar tarefa
5 - Listar tarefas
0 - Sair
========================================
```

### Submenu de Listagem

Ao selecionar a opção "5 - Listar tarefas", um submenu é exibido:

```text
========================================
LISTAR TAREFAS
========================================
1 - Listar todas as tarefas
2 - Listar somente tarefas concluídas
3 - Listar somente tarefas pendentes
0 - Voltar ao menu principal
========================================
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
- Implementação de menus hierárquicos e submenus
- Filtragem de dados com list comprehensions
- Workflow profissional com Git (branches, commits, pull requests)

---

## Possíveis melhorias futuras

- Adicionar, remover ou concluir múltiplas tarefas de uma só vez
- Interface gráfica ou versão web
- Busca de tarefas por descrição
- Ordenação de tarefas (por data, status, etc.)

---

## Autor

**Kauan Melo**
[GitHub](https://github.com/Sahvyt)
[LinkedIn](https://www.linkedin.com/in/kauan-melo-8b72a0305/)
