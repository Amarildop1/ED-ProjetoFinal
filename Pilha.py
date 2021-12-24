from PilhaException import PilhaException
      
class Pilha:
    def __init__(self):
        self.__dado = []

    def estaVazia(self):
        return True if (len(self.__dado) == 0) else False

    def tamanho(self):
        return len(self.__dado)

    def topo(self): # Retorna o conteúdo que está no topo da pilha
        try:
            return self.__dado[-1]
        except IndexError:
            print("  Pilha Vazia.")

    def empilha(self, valor ): # Adiciona um novo elemento ao topo da pilha
        self.__dado.append(valor)

    def desempilha(self):
        #Remove um elemento do topo da pilha e devolve(retorna) o conteudo removido.
        try:
            return self.__dado.pop()
        except IndexError:
            raise PilhaException(f'A Pilha está Vazia. Não é possível remover')

    def __str__(self):
        return self.__dado.__str__()

