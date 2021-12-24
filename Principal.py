from Pilha import Pilha
from PilhaException import PilhaException
from RegexURL import ValidacaoDeSites
import re
from Browser import Browser
from Dns import Dns

#################### PROGRAMA PRINCIPAL ####################
if __name__ == "__main__":
    historico = Pilha()
    navegador = Browser()
    dns = Dns()
    print("\n ============================== INICIO DO BROWSER ============================== ")

    menu = True
    while menu:
        print(f'\n  Histórico de Visitas: {historico}')
        if (historico.topo() != None):
            print(f'\n  HOME: {historico.topo()}')
        else:
            print("\n  HOME: ")

        print("""\n  Comandos úteis: 
                #add para adicionar uma nova URL.
                #showhist para exibir o histórico de páginas.
                #back para retornar a última pagina visitada.
                #help para informações sobre os comandos.
                #sair para encerrar o programa. \n""")

        entrada = input("  Digite um comando ou uma URL para navegar: ")
        print(" ............................................................................... ")
        
        if (entrada[0] == "#"):
            if (entrada == "#add" or entrada == "#ADD"): 
                navegador.adicionarURL(historico) # Método adicionar da classe Browser
            elif (entrada == "#showhist" or entrada == "#SHOWHIST"):  
                navegador.mostrarHistorico(historico) # Método mostrarHistorico da classe Browser
            elif (entrada == "#back" or entrada == "#BACK"):
                navegador.voltarUmaPagina(historico) # Método voltarPagina da classe Browser
            elif ( (entrada == "#help") or (entrada == "#HELP") ):
                navegador.ajudaDosComandos()
            elif ( (entrada == "#sair") or (entrada == "#SAIR") ):
                menu = False
        else:
            existeURL = dns.verificaSeExisteURLnoBanco(entrada)

            if existeURL:
                navegador.acessarPaginaInterna(entrada)
                historico.empilha(entrada)
            else:
                print(" \n \t\t Use o comando #add se quiser adicionar uma nova URL. \n")

        print(" ............................................................................... ")

    print("\n \t\t\t FIM DO PROGRAMA \n")