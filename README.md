# Gerenciador de Tarefas em Python (CLI)

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Versão](https://img.shields.io/badge/versão-2.1-blue)
![Python](https://img.shields.io/badge/python-3.10+-green)

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

## Roadmap do Projeto

Este projeto está em desenvolvimento ativo seguindo um roadmap planejado para demonstrar evolução técnica desde conceitos básicos até implementações complexas.

### Versões Concluídas

#### v1.0 - CLI Básico
- Adicionar, listar e concluir tarefas
- Persistência em JSON
- Menu interativo
- Validação de entrada do usuário

#### v2.0 - Sistema de IDs Únicos
- IDs permanentes e exclusivos
- Busca por ID ao invés de índice
- Correção de bugs críticos de índices
- Padronização de emojis de status

#### v2.1 - Filtragem e Edição
- Submenu de listagem hierárquico
- Filtros por status (todas/concluídas/pendentes)
- Edição de descrição de tarefas
- Remoção de tarefas por ID

### Em Desenvolvimento

#### v3.0 - Operações em Lote
- Adicionar múltiplas tarefas de uma vez
- Remover múltiplas tarefas por lista de IDs
- Concluir múltiplas tarefas simultaneamente
- Limpar todas as tarefas concluídas
- Submenu para operações em lote

### Próximas Versões Planejadas

#### v3.1 - Sistema de Timestamps
- Data e hora de criação automática
- Data e hora de conclusão
- Histórico de modificações
- Ordenação por data

#### v3.2 - Prioridades e Categorias
- Sistema de prioridades (alta/média/baixa)
- Categorias personalizadas
- Tags para organização
- Filtros avançados combinados

#### v4.0 - Interface Desktop (GUI)
- Aplicação desktop com Tkinter
- Interface gráfica intuitiva
- Mesma funcionalidade do CLI
- Tema claro/escuro

#### v5.0 - Versão Web (MVP)
- Backend com Flask/FastAPI
- Interface web responsiva
- Acesso via navegador
- API REST para operações

#### v6.0 - UI/UX Profissional
- Design moderno com Tailwind CSS
- Animações e transições suaves
- Mobile-first e responsivo
- Dashboard com estatísticas

#### v7.0 - Integração com IA
- Sugestões inteligentes de tarefas
- Categorização automática
- Priorização baseada em padrões
- Assistente virtual para gerenciamento

---

## Objetivo do Projeto

Desenvolver um gerenciador de tarefas completo e escalável que evolui desde uma aplicação CLI básica até uma solução web moderna com recursos de IA, demonstrando:

- Domínio de fundamentos de programação
- Capacidade de planejamento e execução de longo prazo
- Evolução técnica progressiva
- Aplicação de boas práticas de desenvolvimento
- Versatilidade em diferentes tipos de interface (CLI, Desktop, Web)

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
- Planejamento e documentação de roadmap de projeto

---

## Tecnologias Utilizadas

- **Python 3.10+** - Linguagem principal
- **JSON** - Persistência de dados
- **Git/GitHub** - Controle de versão e colaboração

### Futuras Tecnologias (Planejadas)

- **Tkinter** - Interface desktop (v4.0)
- **Flask/FastAPI** - Backend web (v5.0)
- **HTML/CSS/JavaScript** - Frontend web (v5.0+)
- **Tailwind CSS** - Framework CSS moderno (v6.0)
- **Claude/OpenAI API** - Integração com IA (v7.0)

---

## Autor

**Kauan Melo**
[GitHub](https://github.com/Sahvyt) • [LinkedIn](https://www.linkedin.com/in/kauan-melo-8b72a0305/)

---

## Licença

Este projeto é de código aberto e está disponível para fins educacionais.
