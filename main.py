import json
import os

CAMINHO_ARQUIVO = os.path.join(os.path.dirname(__file__), "tarefas.json")


def carregar_tarefas():
    if not os.path.exists(CAMINHO_ARQUIVO):
        return []

    try:
        with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Erro ao carregar tarefas: {e}")
        return []


def salvar_tarefas(tarefas):
    try:
        with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
            json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Erro ao salvar tarefas: {e}")


def obter_proximo_id(tarefas):
    """Retorna o próximo ID disponível"""
    if not tarefas:
        return 1
    return max(tarefa["id"] for tarefa in tarefas) + 1


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
    salvar_tarefas(tarefas)
    print(f"Tarefa #{tarefa['id']} adicionada com sucesso!")


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
        salvar_tarefas(tarefas)
        print(f"\n{contador} tarefa(s) adicionada(s) com sucesso!")
    else:
        print("\nNenhuma tarefa foi adicionada.")


def listar_tarefas(tarefas, filtro=None):
    tarefas_filtradas = tarefas

    if filtro == "concluidas":
        tarefas_filtradas = [t for t in tarefas if t["concluida"]]
    elif filtro == "pendentes":
        tarefas_filtradas = [t for t in tarefas if not t["concluida"]]

    if len(tarefas_filtradas) == 0:
        if filtro == "concluidas":
            print("Nenhuma tarefa concluída cadastrada.")
        elif filtro == "pendentes":
            print("Nenhuma tarefa pendente cadastrada.")
        else:
            print("Nenhuma tarefa cadastrada.")
        return

    for tarefa in tarefas_filtradas:
        status = "✓" if tarefa["concluida"] else "⏳"
        print(f"#{tarefa['id']} [{status}] {tarefa['descricao']}")


def encontrar_tarefa_por_id(tarefas, id_tarefa):
    """Encontra uma tarefa pelo ID"""
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
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

    if tarefa["concluida"]:
        print("Essa tarefa já está concluída.")
        return

    tarefa["concluida"] = True
    salvar_tarefas(tarefas)
    print(f"Tarefa #{id_tarefa} marcada como concluída!")


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

    tarefas.remove(tarefa)
    salvar_tarefas(tarefas)
    print(f"Tarefa #{id_tarefa} '{tarefa['descricao']}' removida com sucesso!")


def remover_multiplas_tarefas(tarefas):
    if len(tarefas) == 0:
        print("Não há tarefas para remover.")
        return

    print("\nRemover múltiplas tarefas (Enter vazio para finalizar)")
    print("=" * 40)
    listar_tarefas(tarefas)
    print("=" * 40)

    contador = 0

    while True:
        entrada = input(f"Tarefa {contador + 1}: ").strip()

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

        tarefas.remove(tarefa)
        contador += 1
        print(f"  → Tarefa #{id_tarefa} removida!")

    if contador > 0:
        salvar_tarefas(tarefas)
        print(f"\n{contador} tarefa(s) removida(s) com sucesso!")
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

    tarefa["descricao"] = nova_descricao
    salvar_tarefas(tarefas)
    print(
        f"Tarefa #{id_tarefa} editada com sucesso! Nova descrição: '{nova_descricao}'")


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
            case "0":
                salvar_tarefas(tarefas)
                print("Saindo...")
                break
            case _:
                print("Opção inválida.")


if __name__ == "__main__":
    main()
