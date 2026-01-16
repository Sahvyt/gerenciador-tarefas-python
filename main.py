from storage import carregar_tarefas, salvar_tarefas
from tasks import (
    adicionar_tarefa,
    remover_tarefa,
    concluir_tarefa,
    editar_tarefa,
    menu_listar_tarefas,
    menu_gerenciar_tarefas
)


def menu():
    print("\n" + "="*40)
    print("1 - Adicionar tarefa")
    print("2 - Remover tarefa")
    print("3 - Concluir tarefa")
    print("4 - Editar tarefa")
    print("5 - Listar tarefas")
    print("6 - Gerenciar múltiplas tarefas")
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
                menu_gerenciar_tarefas(tarefas)
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
