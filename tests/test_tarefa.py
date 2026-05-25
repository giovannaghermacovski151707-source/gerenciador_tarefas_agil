from src.tarefa import Tarefa


def test_criar_tarefa():
    tarefa = Tarefa(
        1,
        "Estudar Python",
        "Fazer exercícios"
    )

    assert tarefa.id == 1
    assert tarefa.titulo == "Estudar Python"
    assert tarefa.descricao == "Fazer exercícios"