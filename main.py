from controllers.no import No
from termcolor import colored

import libs.verificacoes
import libs.arvore
import libs.inicio
import libs.jogadas
import libs.jogadaTeste

def start():
    """Função que inicia o jogo
    """
    #Criação do no pai
    pai = No()
    
    #chamadas inicias
    libs.inicio.BemVindo()
    jogador = libs.inicio.iniciaJogo()
    profUser = libs.inicio.receberProfundidade()
    
    #Configuração do tabuleiro que é um dicionário
    tabuleiroJogada = {
        1: ' ', 2: ' ', 3: ' ',
        4: ' ', 5: ' ', 6: ' ',
        7: ' ', 8: ' ', 9: ' '
    }
    print(colored("**********************************", 'yellow'))
    print(colored("Em alguns segundos vamos iniciar nosso jogo!!!!", 'yellow'))
    libs.arvore.preencheArvore(pai,jogador)
    libs.arvore.MinMax(pai,jogador)
    print(colored("Começando o jogo!!!!!! Boa sorteee!!!!", 'yellow'))
    libs.jogadas.jogada(pai,jogador,tabuleiroJogada,0,profUser)
    
if __name__ == '__main__':
    start()
    
    
