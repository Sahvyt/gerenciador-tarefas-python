# Gerenciador de Tarefas em Python (CLI)

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Versão](https://img.shields.io/badge/versão-3.0.2-blue)
![Python](https://img.shields.io/badge/python-3.10+-green)

Aplicação de linha de comando (CLI) desenvolvida em Python para gerenciamento de tarefas, com **IDs únicos e permanentes**, **operações em lote** e **persistência em arquivo JSON**.

Projeto focado em praticar fundamentos sólidos de programação, organização de código e tratamento de erros em aplicações CLI.

---

## Funcionalidades

* Sistema de IDs únicos, incrementais e reutilizáveis
* Adição, edição, conclusão e remoção de tarefas por ID
* Operações em lote (adicionar, remover e concluir múltiplas tarefas)
* Listagem de tarefas (todas, concluídas ou pendentes)
* Persistência automática em arquivo JSON
* Validação de dados ao carregar tarefas
* Interface simples via terminal

---

## Execução

### Requisitos

* Python 3.10 ou superior

### Como rodar

```bash
python main.py
```

---

## Exemplo de uso

```text
#1 [✓] Comprar leite
#5 [⏳] Estudar Python
#12 [⏳] Fazer exercícios
```

Os IDs são permanentes e reutilizados somente através da operação "Reordenar tarefas"

---

## Decisões Técnicas

### IDs permanentes

Os IDs não dependem da posição da tarefa na lista. Eles são sempre calculados a partir do maior ID existente, evitando bugs comuns causados por índices e garantindo consistência após remoções.
    - Reordenação implementada, evitando o crescimento contínuo dos IDs.

### Persistência em JSON

O JSON foi escolhido por ser simples, legível e adequado para uma aplicação CLI. Ao carregar o arquivo, apenas tarefas com estrutura válida são consideradas.

### Rollback em caso de erro

Sempre que uma operação altera o estado das tarefas, o salvamento é tentado imediatamente. Caso o salvamento falhe, o estado anterior é restaurado em memória, evitando inconsistências entre a lista e o arquivo.

### Operações em lote interativas

As operações em lote permitem múltiplas entradas em sequência, com validação individual e possibilidade de encerramento a qualquer momento.

### Modularização

O código foi modularizado para separar responsabilidades:
    - ```main.py```: interface e fluxo do programa
    - ```tasks.py```: regras de negócio
    - ```storage.py```: persistência em arquivo JSON
    - ```models.py```: validações e utilitários
---

## Roadmap

* v1.0: CLI básico com persistência
* v2.0: Sistema de IDs únicos
* v2.1: Filtros e edição de tarefas
* v3.0: Operações em lote
* v4.0: Interface desktop
* v5.0: Versão web

---

## Tecnologias

* Python 3.10+
* JSON
* Git / GitHub

---

## Autor

**Kauan Melo**
[GitHub](https://github.com/Sahvyt) • [LinkedIn](https://www.linkedin.com/in/kauan-melo-8b72a0305/)

---

## Licença

Projeto open-source com fins educacionais.
