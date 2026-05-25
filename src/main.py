from tarefa import Tarefa

tarefas = []


def criar_tarefa():
    titulo = input("Digite o título: ")
    descricao = input("Digite a descrição: ")

    tarefa = Tarefa(
        len(tarefas) + 1,
        titulo,
        descricao
    )

    tarefas.append(tarefa)

    print("Tarefa criada com sucesso!")


def listar_tarefas():
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
        return

    for tarefa in tarefas:
        print(tarefa.exibir())


def atualizar_tarefa():
    id_tarefa = int(input("Digite o ID da tarefa: "))

    for tarefa in tarefas:
        if tarefa.id == id_tarefa:
            tarefa.titulo = input("Novo título: ")
            tarefa.descricao = input("Nova descrição: ")

            print("Tarefa atualizada com sucesso!")
            return

    print("Tarefa não encontrada.")


def excluir_tarefa():
    id_tarefa = int(input("Digite o ID da tarefa: "))

    for tarefa in tarefas:
        if tarefa.id == id_tarefa:
            tarefas.remove(tarefa)

            print("Tarefa removida com sucesso!")
            return

    print("Tarefa não encontrada.")


while True:
    print("\n===== MENU =====")
    print("1 - Criar tarefa")
    print("2 - Listar tarefas")
    print("3 - Atualizar tarefa")
    print("4 - Excluir tarefa")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        criar_tarefa()

    elif opcao == "2":
        listar_tarefas()

    elif opcao == "3":
        atualizar_tarefa()

    elif opcao == "4":
        excluir_tarefa()

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")