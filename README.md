# Gerenciador de Tarefas em Python (CLI)

Aplicação de linha de comando desenvolvida em Python para gerenciar tarefas com sistema de identificação único, permitindo adicionar, listar, editar, concluir e remover tarefas com persistência em arquivo JSON.

Este projeto foi criado com foco em praticar lógica de programação, manipulação de arquivos, estruturas de dados e organização de código em Python.

---

## Funcionalidades

- **Sistema de IDs únicos**: Cada tarefa recebe um ID permanente e exclusivo
- Adicionar novas tarefas
- Remover tarefas por ID
- Marcar tarefas como concluídas
- Editar descrição de tarefas existentes
- Listar tarefas com filtros por status:
  - Listar todas as tarefas
  - Listar somente tarefas concluídas
  - Listar somente tarefas pendentes
- Persistência de dados em arquivo JSON
- Interface simples via terminal (CLI) com menu hierárquico
- IDs permanentes que não mudam mesmo após remoções

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

### Visualização de Tarefas

As tarefas são exibidas com seus IDs únicos e status visual:

```text
#1 [✓] Comprar leite
#5 [⏳] Estudar Python
#12 [⏳] Fazer exercícios
```

**Nota:** O ID é permanente - se você remover a tarefa #5, ela nunca mais será reutilizada. A próxima tarefa criada será #13.

As tarefas são salvas automaticamente no arquivo `tarefas.json`.

---

## Sistema de IDs

Este gerenciador utiliza um sistema de identificação único para cada tarefa:

- **IDs são incrementais**: A primeira tarefa é #1, a segunda #2, e assim por diante
- **IDs são permanentes**: Uma vez atribuído, o ID nunca muda
- **IDs nunca são reutilizados**: Se você remover a tarefa #50, nenhuma tarefa futura receberá o ID #50
- **Operações usam IDs**: Todas as ações (editar, remover, concluir) são feitas através do ID da tarefa

Este sistema garante:
- Não há confusão ao filtrar tarefas
- Referências às tarefas são sempre corretas
- Facilita futuras implementações (datas, prioridades, etc.)

---

## O que aprendi com esse projeto

- Leitura e escrita de arquivos JSON em Python
- Persistência de dados em aplicações simples
- Organização de um programa em funções
- Validação de entrada do usuário
- Uso de estruturas de dados como listas e dicionários
- Controle de fluxo em aplicações CLI
- Uso de `match/case` (Python 3.10+) como alternativa moderna a `if/elif/else`
- Implementação de menus hierárquicos e submenus
- Filtragem de dados com list comprehensions
- Sistema de identificação única (IDs) para registros
- Busca e manipulação de dados por identificador
- Resolução de bugs relacionados a índices vs identificadores
- Workflow profissional com Git (branches, commits, pull requests)

---

## Possíveis melhorias futuras

- Adicionar, remover ou concluir múltiplas tarefas de uma só vez
- Adicionar timestamps (data/hora de criação e conclusão)
- Priorização de tarefas
- Categorias ou tags
- Busca de tarefas por descrição
- Ordenação de tarefas (por data, status, prioridade)
- Função de reenumerar IDs (resetar para 1, 2, 3...)
- Interface gráfica (GUI) ou versão web
- Integração com IA para gerenciamento inteligente de tarefas

---

## Autor

**Kauan Melo**
[GitHub](https://github.com/Sahvyt)
[LinkedIn](https://www.linkedin.com/in/kauan-melo-8b72a0305/)
