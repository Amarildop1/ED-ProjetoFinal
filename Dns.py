
from Arquivo import Arquivo

class Dns:

    #Se existir mostra "PÁGINA ENCONTRADA! senão PÁGINA NÃO ENCONTRADA!"        
    def verificaSeExisteURLnoBanco(self, url):
        for linha in Arquivo.ler_arquivo("db-urls.txt"):
            linha = linha.strip()
            vetorURL = linha.split('/')
            if linha == url:
                print(f'\n\n  URL: {url}')
                print("\n \t\t\t PÁGINA ENCONTRADA :) \n\n")
                return url
            elif '/' in linha and linha == url:
                vetorURL = linha.split('/')
                print(f'\n\n  URL: {url}')
                print("\n \t\t\t Página Encontrada :) \n\n")
                print(f'\n  Links Disponíveis: \n    /{vetorURL[1]} \n   \t /{vetorURL[-1]} \n')
                return vetorURL
        else:
            print("\n\n \t\t ERRO 404! - PÁGINA NÃO ENCONTRADA. :( ")
            print("\n\n \t\t Verifique a URL digitada e tente novamente. \n")
            return False
        return True
    ########################################################################