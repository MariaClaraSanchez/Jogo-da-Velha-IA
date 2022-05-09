from controllers.no import No
from termcolor import colored
import libs.verificacoes
import libs.arvore
import random

def jogada(raiz:No,jogador:str,dicJogada:str,profundidade:int,profDesejada:int):
    """Função onde é realizada todas as jogadas

    Args:
        raiz (No): no pai, o que criamos e preenchemos
        jogador (str): jogador
        dicJogada (str): dicionário para ser o tabuleiro
        profundidade (int): profundidade
        profDesejada (int): profundidade que o usuário deseja, ou seja a dificuldade do jogo
    """
    profundidade = profundidade+1
    ganhador = libs.verificacoes.checkGanhador(dicJogada)
    if ganhador == 'X':
        libs.verificacoes.printTabuleiro(dicJogada)
        print("Você perdeu!")
        exit()
    elif ganhador == 'O':
        print("Você ganhou! Muito bem")
        libs.verificacoes.printTabuleiro(dicJogada)
        exit()
    elif ganhador == '-':
        libs.verificacoes.printTabuleiro(dicJogada)
        print("Deu empate!")
        exit()
    else:
        libs.verificacoes.printTabuleiro(dicJogada)
        print("\n*******************\n")
    
    if jogador == 'X':
        
        
        if profundidade >= profDesejada:
            print("Modo Aleatório!")
            jogada_aleatoria_maquina = jogadaAleatoria(dicJogada)
            jogada(raiz,'O',jogada_aleatoria_maquina,profundidade,profDesejada)
            
        
        no_melhorJogada = melhoresPossiveisJogadas(raiz,dicJogada)
        
        jogada(no_melhorJogada,'O',dicJogada,profundidade,profDesejada)
        
    else:
        jogaUser = jogadaUser(dicJogada,jogador)
        
        for i in raiz.listaFilhos:
            if i.board == dicJogada:
                jogada(i,'X',dicJogada,profundidade,profDesejada)
        
        jogada(raiz,'X',jogaUser,profundidade,profDesejada) 

def melhoresPossiveisJogadas(raiz:No,dictJogada:dict) -> dict:
    """Analisa as melhores jogadas

    Args:
        raiz (No): recebe o no pai
        dictJogada (dict): recebe o dicionário de jogadas

    Returns:
        No: retorna o filho preenchido na melhor posição
    """
    melhoresValoresDaMaquina = []
        
    maior = -10
        
    for i in range(len(raiz.listaFilhos)):
        if raiz.listaFilhos[i].valorMinMax > maior: 
            maior = raiz.listaFilhos[i].valorMinMax

    for i in range(len(raiz.listaFilhos)):
        if raiz.listaFilhos[i].valorMinMax == maior:
            melhoresValoresDaMaquina.append(raiz.listaFilhos[i])

    filho = No()   
    
    board = JogadaDosMelhores(dictJogada,melhoresValoresDaMaquina)
    
    filho.board = board.copy()
    
    return filho

def jogadaUser(tabuleiro:dict,jogador:str) -> dict:
    """Jogada do usuário

    Args:
        tabuleiro (dict): recebe um tabuleiro
        jogador (str): recebe o 'O'

    Returns:
        dict: retorna o tabuleiro preenchido
    """
    posicao = int(input("Digite a posição que deseja jogar:  "))
    
    if tabuleiro[posicao] != ' ':
        print(colored("Posição já utilizada, digite novamente!!!",'red'))
        posicao = int(input("Digite novamente a posição que deseja jogar:  "))

    libs.verificacoes.InserirJogada(tabuleiro,jogador,posicao)
    
    return tabuleiro

def JogadaDosMelhores(tabuleiro:dict,melhores:list):
    """Função que pega todas as possiveis chances de um filho e sorteia um deles

    Args:
        tabuleiro (dict): tabuleiro utilizado
        melhores (list): list do tipo inteiro

    Returns:
        dict: retorna o tabuleiro de jogadas
    """
    if melhores == []:
        pos = 1
    else:
        pos = random.choice(melhores)
        # print(f'Valor da posicao do aleatorio dos melhores {pos}')
        
    board = libs.verificacoes.InserirJogada(tabuleiro,'X',pos)
    return board

def jogadaAleatoria(tabuleiro:dict):
    """Função que sorteia algum número aleatório para jogar

    Args:
        tabuleiro (dict): tabuleiro da jogada

    Returns:
        dict: retorna o tabuleiro de volta
    """
    aux = []
    for key in tabuleiro.keys():
        if tabuleiro[key] == ' ':
            aux.append(key)
            
    pos = random.choice(aux)
    if pos == 0:
        pos = random(aux)
        
    print(f'Valor da posicao do aleatorio {pos}')
    
    dic = libs.verificacoes.InserirJogada(tabuleiro,'X',pos)    
    
    return dic
