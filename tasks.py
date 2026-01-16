from models import obter_proximo_id, encontrar_tarefa_por_id, validar_estrutura_tarefa
from storage import salvar_tarefas


def adicionar_tarefa(tarefas):
    descricao = input("Descrição da tarefa: ").strip()

    if descricao == "":
        print("A descrição não pode ser vazia.")
        return

    tarefa = {
        "id": obter_proximo_id(tarefas),
        "descricao": descricao,
        "concluida": False
    }

    tarefas.append(tarefa)
    if salvar_tarefas(tarefas):
        print(f"Tarefa #{tarefa['id']} adicionada com sucesso!")
    else:
        print(
            "Erro: A tarefa foi adicionada à lista, mas não foi possível salvar no arquivo.")
        tarefas.remove(tarefa)


def adicionar_multiplas_tarefas(tarefas):
    print("\nAdicionar múltiplas tarefas (Enter vazio para finalizar)")
    print("=" * 40)

    contador = 0

    while True:
        descricao = input(f"Tarefa {contador + 1}: ").strip()

        if descricao == "":
            break

        tarefa = {
            "id": obter_proximo_id(tarefas),
            "descricao": descricao,
            "concluida": False
        }

        tarefas.append(tarefa)
        contador += 1
        print(f"  → Tarefa #{tarefa['id']} adicionada!")

    if contador > 0:
        if salvar_tarefas(tarefas):
            print(f"\n{contador} tarefa(s) adicionada(s) com sucesso!")
        else:
            print(
                f"\nErro: {contador} tarefa(s) foram adicionadas à lista, mas não foi possível salvar no arquivo.")
            for _ in range(contador):
                tarefas.pop()
    else:
        print("\nNenhuma tarefa foi adicionada.")


def listar_tarefas(tarefas, filtro=None):
    tarefas_validas = [t for t in tarefas if validar_estrutura_tarefa(t)]
    tarefas_filtradas = tarefas_validas

    if filtro == "concluidas":
        tarefas_filtradas = [
            t for t in tarefas_validas if t.get("concluida", False)]
    elif filtro == "pendentes":
        tarefas_filtradas = [
            t for t in tarefas_validas if not t.get("concluida", False)]

    if len(tarefas_filtradas) == 0:
        if filtro == "concluidas":
            print("Nenhuma tarefa concluída cadastrada.")
        elif filtro == "pendentes":
            print("Nenhuma tarefa pendente cadastrada.")
        else:
            print("Nenhuma tarefa cadastrada.")
        return

    for tarefa in tarefas_filtradas:
        status = "✓" if tarefa.get("concluida", False) else "⏳"
        print(
            f"#{tarefa.get('id', '?')} [{status}] {tarefa.get('descricao', 'Sem descrição')}")


def concluir_tarefa(tarefas):
    if len(tarefas) == 0:
        print("Não há tarefas para concluir.")
        return

    listar_tarefas(tarefas)

    try:
        id_tarefa = int(input("Digite o ID da tarefa a concluir: "))
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return

    tarefa = encontrar_tarefa_por_id(tarefas, id_tarefa)

    if not tarefa:
        print("Tarefa não encontrada.")
        return

    if tarefa.get("concluida", False):
        print("Essa tarefa já está concluída.")
        return

    tarefa["concluida"] = True
    if salvar_tarefas(tarefas):
        print(f"Tarefa #{id_tarefa} marcada como concluída!")
    else:
        print("Erro: A tarefa foi marcada como concluída, mas não foi possível salvar no arquivo.")
        tarefa["concluida"] = False


def concluir_multiplas_tarefas(tarefas):
    if len(tarefas) == 0:
        print("Não há tarefas para concluir.")
        return

    print("\nConcluir múltiplas tarefas (Enter vazio para finalizar)")
    print("=" * 40)
    listar_tarefas(tarefas)
    print("=" * 40)

    contador = 0
    ids_marcados = []

    while True:
        entrada = input(
            "Digite o ID da tarefa (ou Enter para finalizar): ").strip()

        if entrada == "":
            break

        try:
            id_tarefa = int(entrada)
        except ValueError:
            print("  → Entrada inválida. Digite um número ou Enter para finalizar.")
            continue

        tarefa = encontrar_tarefa_por_id(tarefas, id_tarefa)
        if not tarefa:
            print(f"  → Tarefa #{id_tarefa} não encontrada. Tente novamente.")
            continue

        if tarefa.get("concluida", False):
            print(f"  → Tarefa #{id_tarefa} já está concluída. Ignorando...")
            continue

        tarefa["concluida"] = True
        ids_marcados.append(id_tarefa)
        contador += 1
        print(f"  → Tarefa #{id_tarefa} marcada como concluída!")

    if contador > 0:
        if salvar_tarefas(tarefas):
            print(
                f"\n{contador} tarefa(s) marcada(s) como concluída(s) com sucesso!")
        else:
            print(
                f"\nErro: {contador} tarefa(s) foram marcadas como concluídas, mas não foi possível salvar no arquivo.")
            for id_tarefa in ids_marcados:
                tarefa = encontrar_tarefa_por_id(tarefas, id_tarefa)
                if tarefa:
                    tarefa["concluida"] = False
    else:
        print("\nNenhuma tarefa foi marcada como concluída.")


def remover_tarefa(tarefas):
    if len(tarefas) == 0:
        print("Não há tarefas para remover.")
        return

    listar_tarefas(tarefas)

    try:
        id_tarefa = int(input("Digite o ID da tarefa a remover: "))
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return

    tarefa = encontrar_tarefa_por_id(tarefas, id_tarefa)

    if not tarefa:
        print("Tarefa não encontrada.")
        return

    descricao_tarefa = tarefa.get('descricao', '')
    tarefas.remove(tarefa)
    if salvar_tarefas(tarefas):
        print(
            f"Tarefa #{id_tarefa} '{descricao_tarefa}' removida com sucesso!")
    else:
        print(
            "Erro: A tarefa foi removida da lista, mas não foi possível salvar no arquivo.")
        tarefas.append(tarefa)


def remover_multiplas_tarefas(tarefas):
    if len(tarefas) == 0:
        print("Não há tarefas para remover.")
        return

    print("\nRemover múltiplas tarefas (Enter vazio para finalizar)")
    print("=" * 40)
    listar_tarefas(tarefas)
    print("=" * 40)

    contador = 0
    ids_removidos = set()
    tarefas_removidas = []

    while True:
        entrada = input(
            "Digite o ID da tarefa (ou Enter para finalizar): ").strip()

        if entrada == "":
            break

        try:
            id_tarefa = int(entrada)
        except ValueError:
            print("  → Entrada inválida. Digite um número ou Enter para finalizar.")
            continue

        if id_tarefa in ids_removidos:
            print(
                f"  → Tarefa #{id_tarefa} já foi removida nesta sessão. Ignorando...")
            continue

        tarefa = encontrar_tarefa_por_id(tarefas, id_tarefa)
        if not tarefa:
            print(f"  → Tarefa #{id_tarefa} não encontrada. Tente novamente.")
            continue

        tarefas.remove(tarefa)
        ids_removidos.add(id_tarefa)
        tarefas_removidas.append(tarefa)
        contador += 1
        print(f"  → Tarefa #{id_tarefa} removida!")

    if contador > 0:
        if salvar_tarefas(tarefas):
            print(f"\n{contador} tarefa(s) removida(s) com sucesso!")
        else:
            print(
                f"\nErro: {contador} tarefa(s) foram removidas da lista, mas não foi possível salvar no arquivo.")
            for tarefa in tarefas_removidas:
                tarefas.append(tarefa)
    else:
        print("\nNenhuma tarefa foi removida.")


def editar_tarefa(tarefas):
    if len(tarefas) == 0:
        print("Não há tarefas para editar.")
        return

    listar_tarefas(tarefas)

    try:
        id_tarefa = int(input("Digite o ID da tarefa a editar: "))
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return

    tarefa = encontrar_tarefa_por_id(tarefas, id_tarefa)

    if not tarefa:
        print("Tarefa não encontrada.")
        return

    nova_descricao = input(
        f"Nova descrição (ou Enter para cancelar): ").strip()

    if nova_descricao == "":
        print("Edição cancelada.")
        return

    descricao_antiga = tarefa["descricao"]
    tarefa["descricao"] = nova_descricao
    if salvar_tarefas(tarefas):
        print(
            f"Tarefa #{id_tarefa} editada com sucesso! Nova descrição: '{nova_descricao}'")
    else:
        print("Erro: A tarefa foi editada, mas não foi possível salvar no arquivo.")
        tarefa["descricao"] = descricao_antiga


def limpar_tarefas_concluidas(tarefas):
    if len(tarefas) == 0:
        print("Não há tarefas para limpar.")
        return

    print("\nLimpar tarefas concluídas")
    print("="*40)
    listar_tarefas(tarefas, filtro="concluidas")
    print("="*40)

    resposta = input(
        "Deseja limpar todas as tarefas concluídas? (s/n): ").strip().lower()

    if resposta == "s":
        for tarefa in tarefas:
            if tarefa.get("concluida", False):
                tarefas.remove(tarefa)
        if salvar_tarefas(tarefas):
            print("Tarefas concluídas limpas com sucesso!")
        else:
            print(
                "Erro: As tarefas foram removidas da lista, mas não foi possível salvar no arquivo.")
            for tarefa in tarefas:
                if tarefa.get("concluida", False):
                    tarefas.append(tarefa)
    else:
        print("Operação cancelada.")


def reordenar_tarefas(tarefas):
    if len(tarefas) == 0:
        print("Não há tarefas para reordenar.")
        return

    print("\nReordenar tarefas")
    print("="*40)
    listar_tarefas(tarefas)
    print("="*40)

    resposta = input(
        "Deseja reordenar todas as tarefas? (s/n): ").strip().lower()

    if resposta == "s":
        ids_antigos = []

        for i, tarefa in enumerate(tarefas, start=1):
            ids_antigos.append(tarefa["id"])
            tarefa["id"] = i
        if salvar_tarefas(tarefas):
            print("Tarefas reordenadas com sucesso!")
        else:
            print(
                "Erro: As tarefas foram reordenadas, mas não foi possível salvar no arquivo.")
            i = 0
            for tarefa, id_antigo in zip(tarefas, ids_antigos):
                tarefa["id"] = id_antigo
    else:
        print("Operação cancelada.")


def menu_listar_tarefas(tarefas):
    while True:
        print("\n" + "="*40)
        print("LISTAR TAREFAS")
        print("="*40)
        print("1 - Listar todas as tarefas")
        print("2 - Listar somente tarefas concluídas")
        print("3 - Listar somente tarefas pendentes")
        print("0 - Voltar ao menu principal")
        print("="*40)

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                listar_tarefas(tarefas, filtro=None)
            case "2":
                listar_tarefas(tarefas, filtro="concluidas")
            case "3":
                listar_tarefas(tarefas, filtro="pendentes")
            case "0":
                break
            case _:
                print("Opção inválida.")


def menu_gerenciar_tarefas(tarefas):
    while True:
        print("\n" + "="*40)
        print("GERENCIAR TAREFAS")
        print("="*40)
        print("1 - Adicionar múltiplas tarefas")
        print("2 - Remover múltiplas tarefas")
        print("3 - Concluir múltiplas tarefas")
        print("4 - Limpar tarefas concluídas")
        print("5 - Reordenar tarefas")
        print("0 - Voltar ao menu principal")
        print("="*40)

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                adicionar_multiplas_tarefas(tarefas)
            case "2":
                remover_multiplas_tarefas(tarefas)
            case "3":
                concluir_multiplas_tarefas(tarefas)
            case "4":
                limpar_tarefas_concluidas(tarefas)
            case "5":
                reordenar_tarefas(tarefas)
            case "0":
                break
            case _:
                print("Opção inválida.")
