class Arquivo:
    def ler_arquivo(nome_arquivo):
        with open(nome_arquivo, encoding="utf8") as arquivo:
            return arquivo.readlines()