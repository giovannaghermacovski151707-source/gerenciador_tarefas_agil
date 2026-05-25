class Tarefa:
    def __init__(self, id, titulo, descricao):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao

    def exibir(self):
        return f"{self.id} - {self.titulo}: {self.descricao}"