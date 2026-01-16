import json
import os

CAMINHO_ARQUIVO = os.path.join(os.path.dirname(__file__), "tarefas.json")


def validar_estrutura_tarefa(tarefa):
    if not isinstance(tarefa, dict):
        return False
    return all(key in tarefa for key in ["id", "descricao", "concluida"])


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


def encontrar_tarefa_por_id(tarefas, id_tarefa):
    for tarefa in tarefas:
        if validar_estrutura_tarefa(tarefa) and tarefa.get("id") == id_tarefa:
            return tarefa
    return None


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


def menu():
    print("\n" + "="*40)
    print("1 - Adicionar tarefa")
    print("2 - Remover tarefa")
    print("3 - Concluir tarefa")
    print("4 - Editar tarefa")
    print("5 - Listar tarefas")
    print("6 - Adicionar múltiplas tarefas")
    print("7 - Remover múltiplas tarefas")
    print("8 - Concluir múltiplas tarefas")
    print("0 - Sair")
    print("="*40)


def main():
    tarefas = carregar_tarefas()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                adicionar_tarefa(tarefas)
            case "2":
                remover_tarefa(tarefas)
            case "3":
                concluir_tarefa(tarefas)
            case "4":
                editar_tarefa(tarefas)
            case "5":
                menu_listar_tarefas(tarefas)
            case "6":
                adicionar_multiplas_tarefas(tarefas)
            case "7":
                remover_multiplas_tarefas(tarefas)
            case "8":
                concluir_multiplas_tarefas(tarefas)
            case "0":
                if salvar_tarefas(tarefas):
                    print("Saindo...")
                else:
                    print("Aviso: Não foi possível salvar as alterações antes de sair.")
                    resposta = input(
                        "Deseja sair mesmo assim? (s/n): ").strip().lower()
                    if resposta == "s":
                        print("Saindo...")
                    else:
                        print(
                            "Operação cancelada. As alterações ainda não foram salvas.")
                        continue
                break
            case _:
                print("Opção inválida.")


if __name__ == "__main__":
    main()
