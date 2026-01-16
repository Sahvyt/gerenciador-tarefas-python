def validar_estrutura_tarefa(tarefa):
    if not isinstance(tarefa, dict):
        return False
    return all(key in tarefa for key in ["id", "descricao", "concluida"])


def obter_proximo_id(tarefas):
    if not tarefas:
        return 1

    try:
        ids_validos = [tarefa.get("id") for tarefa in tarefas if validar_estrutura_tarefa(
            tarefa) and isinstance(tarefa.get("id"), int)]

        if not ids_validos:
            return 1

        return max(ids_validos) + 1
    except (ValueError, TypeError):
        return 1


def encontrar_tarefa_por_id(tarefas, id_tarefa):
    for tarefa in tarefas:
        if validar_estrutura_tarefa(tarefa) and tarefa.get("id") == id_tarefa:
            return tarefa
    return None
