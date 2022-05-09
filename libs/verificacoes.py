def checkGanhador(board:dict):
    """Função para retornar o ganhador

    Args:
        board (dict): recebe um dicionário, ou seja o tabuleiro

    Returns:
        str: retorna o ganhador ou vazio caso ainda não tenha ganhador
    """
    
    # Verificando na horizontal
    if ((board[1] == board[2]) and (board[1] == board[3]) and (board[1] != ' ')):
        return board[1]
    elif ((board[4] == board[5]) and (board[4] == board[6]) and (board[4] != ' ')):
        return board[4]
    elif ((board[7] == board[8]) and (board[7] == board[9]) and (board[7] != ' ')):
        return board[7]

        # Verificando na Vertical
    elif ((board[1] == board[4]) and (board[1] == board[7]) and (board[1] != ' ')):
        return board[1]
    elif ((board[2] == board[5]) and (board[2] == board[8]) and (board[2] != ' ')):
        return board[2]
    elif ((board[3] == board[6]) and (board[3] == board[9]) and (board[3] != ' ')):
        return board[3]

        # Verificando na diagonal
    elif ((board[1] == board[5]) and (board[1] == board[9]) and (board[1] != ' ')):
        return board[1]
    elif ((board[7] == board[5]) and (board[7] == board[3]) and (board[7] != ' ')):
            # print("Caiu aqui")
        return board[7]

    # Ainda Está vazio
    else:
        for key in board.keys():
            if espacoVazio(board,key) == True:
                return ' '
       # Deu velha
    return '-'

from termcolor import colored


def printTabuleiro(board:dict):
    """Método que imprimi o tabuleiro

    Args:
        board (dict): recebe o tabuleiro
    """
    print(colored("┌───┬───┬───┐",'magenta'))
    print(f"│ {board [1]} │ {board [2] } │ {board [3]} │")
    print(colored("├───┼───┼───┤", 'magenta'))
    print(f"│ {board [4]} │ {board [5] } │ {board [6]} │")
    print(colored("├───┼───┼───┤", 'magenta'))
    print(f"│ {board [7]} │ {board [8] } │ {board [9]} │")
    print(colored("└───┴───┴───┘",'magenta'))
    
def espacoVazio(board:dict,posicao:int):
    """ Função que analisa as posições que estão vazias


    Args:
        board (dict): recebe o tabuleiro
        posicao (int): posição para ser analisada

    Returns:
        bool: retorna verdadeiro - True ou flaso - True
    """
    
    if board[posicao] == ' ':
        return True
    else:
        return False
        
def InserirJogada(board:dict,caracter:str, posicao:int) -> dict:
    """ Função utilizada para inserir as jogadas

    Args:
        board (dict): tabuleiro que está sendo utilziado para jogar
        caracter (str): qual caracter vai ser inserido, ('X' | 'O')
        posicao (int): posicao que vai ser inserido os dados

    Returns:
        dict: o tabuleiro com a nova jogada
    """
    for key in board.keys():
        if board[key] == ' ' and key == posicao:
            board[key] = caracter
    return board
