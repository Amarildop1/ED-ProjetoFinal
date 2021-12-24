class PilhaException(Exception):
    def __init__(self, msg): # Recebe a mensagem para exibir na exceção
        super().__init__(msg)