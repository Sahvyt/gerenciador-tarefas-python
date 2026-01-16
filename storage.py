import json
import os
from models import validar_estrutura_tarefa

CAMINHO_ARQUIVO = os.path.join(os.path.dirname(__file__), "tarefas.json")


def carregar_tarefas():
    if not os.path.exists(CAMINHO_ARQUIVO):
        return []

    try:
        with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        if not isinstance(dados, list):
            print(
                "Erro: O arquivo de tarefas não contém uma lista válida. Criando nova lista.")
            return []

        tarefas_validas = [t for t in dados if validar_estrutura_tarefa(t)]
        tarefas_invalidas = len(dados) - len(tarefas_validas)

        if tarefas_invalidas > 0:
            print(
                f"Aviso: {tarefas_invalidas} tarefa(s) com estrutura inválida foram ignoradas.")

        return tarefas_validas
    except (json.JSONDecodeError, IOError) as e:
        print(f"Erro ao carregar tarefas: {e}")
        return []


def salvar_tarefas(tarefas):
    try:
        with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
            json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
        return True
    except IOError as e:
        print(f"Erro ao salvar tarefas: {e}")
        return False
