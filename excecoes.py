class Excecao(Exception):

    def __init__(self, mensagem="### Erro: Tente novamente"):
        self.mensagem = mensagem
        super().__init__(self.mensagem)
