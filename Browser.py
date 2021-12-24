from Pilha import Pilha
from RegexURL import ValidacaoDeSites
import re
from Arquivo import Arquivo

class Browser:

    def adicionarURL(self, historico):
        padraoURL = ValidacaoDeSites()
        novaURL = input("\n  Informe uma URL para adicionar: ")

        # Se o padrão for atendido recebe True e empilha
        if (re.match(padraoURL.validarSite(), novaURL) is not None):
            historico.empilha(novaURL)
            print("\n\n \t\t Página adicionada com sucesso! \n\n")
            with open('db-urls.txt', 'a') as arq:
                arq.write(novaURL + '\n')
        else:
            print("\n \t\t URL Inválida! Tente novamente. \n\n")
    
    def mostrarHistorico(self, historico):
        if ( historico.estaVazia() ):
                print("\n\n \t\t\t Histórico Limpo! \n\n")
        else:
            print(f'\n\n  Histórico de Visitas: {historico}')
            print(f'\n  HOME: {historico.topo()} \n\n')


    def voltarUmaPagina(self, historico):
        if ( historico.estaVazia() ):
            print("\n\n \t\t\t Não há página anterior! \n\n")
        elif ( historico.tamanho() == 1 ):
            print("\n\n  Você já chegou na página inicial. Se deseja sair digite o comando #sair! \n\n")
        else:
            print("\n\n  \t\t\t Voltando... \n")
            historico.desempilha()
            if (historico.topo() != None):
                print(f'\n  HOME: {historico.topo()} \n')
            else:
                print("\n  HOME: \n")
    
    def acessarPaginaInterna(self, url):
        if url == 'www.ifpb.edu.br':
            for line in Arquivo.ler_arquivo("ifpb.txt"):
                print(line)
        
        if url == 'www.ifpb.edu.br/tsi':
            for line in Arquivo.ler_arquivo("ifpb-edu-br-tsi.txt"):
                print(line)
    
    def ajudaDosComandos(self):
        print("""\n  Informações úteis: 

                #add :      Use para adicionar uma nova URL no arquivo.
                #showhist : Exibe o histórico de páginas visitadas desde o início.
                            (Não distingue URLs repetidas)
                            (A mais recente está mais a direita)
                #back :     Retorna para a última pagina visitada.
                            (Pode ser utilizado várias vezes)
                            (Consegue voltar até o primeiro site)
                #help :     Informações sobre os comandos.
                #sair :     Encerra o programa. \n""")