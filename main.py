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


def adicionar_tarefa(tarefas):
    descricao = input("Descrição da tarefa: ").strip()

    if descricao == "":
        print("A descrição não pode ser vazia.")
        return

    tarefa = {
        "descricao": descricao,
        "concluida": False
    }

    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso!")


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

    for i, tarefa in enumerate(tarefas_filtradas, start=1):
        status = "✔" if tarefa["concluida"] else "⏳"
        print(f"{i}. [{status}] {tarefa['descricao']}")


def concluir_tarefa(tarefas):
    if len(tarefas) == 0:
        print("Não há tarefas para concluir.")
        return

    listar_tarefas(tarefas)

    try:
        indice = int(input("Digite o número da tarefa a concluir: ")) - 1
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return

    if indice < 0 or indice >= len(tarefas):
        print("Número de tarefa inválido.")
        return

    if tarefas[indice]["concluida"]:
        print("Essa tarefa já está concluída.")
        return

    tarefas[indice]["concluida"] = True
    salvar_tarefas(tarefas)
    print("Tarefa marcada como concluída!")


def remover_tarefa(tarefas):
    if len(tarefas) == 0:
        print("Não há tarefas para remover.")
        return

    listar_tarefas(tarefas)

    try:
        indice = int(input("Digite o número da tarefa a remover: ")) - 1
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return

    if indice < 0 or indice >= len(tarefas):
        print("Número de tarefa inválido.")
        return

    tarefa_removida = tarefas.pop(indice)
    salvar_tarefas(tarefas)
    print(f"Tarefa '{tarefa_removida['descricao']}' removida com sucesso!")


def editar_tarefa(tarefas):
    if len(tarefas) == 0:
        print("Não há tarefas para editar.")
        return

    listar_tarefas(tarefas)

    try:
        indice = int(input("Digite o número da tarefa a editar: ")) - 1
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return

    if indice < 0 or indice >= len(tarefas):
        print("Número de tarefa inválido.")
        return

    tarefa_editada = tarefas[indice]
    nova_descricao = input(
        f"Nova descrição (ou Enter para cancelar): ").strip()

    if nova_descricao == "":
        print("Edição cancelada.")
        return

    tarefa_editada["descricao"] = nova_descricao
    salvar_tarefas(tarefas)
    print(f"Tarefa editada com sucesso! Nova descrição: '{nova_descricao}'")


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
            case "0":
                salvar_tarefas(tarefas)
                print("Saindo...")
                break
            case _:
                print("Opção inválida.")


if __name__ == "__main__":
    main()
