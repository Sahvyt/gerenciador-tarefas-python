import json
import os

CAMINHO_ARQUIVO = os.path.join(os.path.dirname(__file__), "tarefas.json")

def carregar_tarefas():
    if not os.path.exists(CAMINHO_ARQUIVO):
        return []

    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def salvar_tarefas(tarefas):
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)

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
    print("Tarefa adicionada com sucesso!")

def listar_tarefas(tarefas):
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
        return

    for i, tarefa in enumerate(tarefas, start=1):
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
    print("Tarefa marcada como concluída!")

def menu():
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("0 - Sair")

def main():
    tarefas = carregar_tarefas()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "0":
            salvar_tarefas(tarefas)
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
