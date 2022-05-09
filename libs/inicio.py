from termcolor import colored
import libs.verificacoes

def iniciaJogo():
    """Função que recebe quem deve começar o jogo

    Returns:
        string: 'X' - Máquina começa | 'O' - Usuário começa
    """
    print(colored('Quem começa o jogo??\n','magenta'))
    print(colored ('1 - Máquina\n','yellow'))
    print(colored('2 - Você ','cyan'))

    vez = int(input('\nDigite o número: '))
    if vez == 1:
        jogador = 'X'
    else:
        jogador = 'O'
    return jogador

def receberProfundidade():
    """Profundidade que o usuário quer, o seja a dificuldade do jogo

    Returns:
        int: retorna um valor inteiro
    """
    prof = int(input("Qual a dificuldade do jogo? 1 a 9: "))
    if prof<1 and prof>9:
        print("Digite uma profundidade válida!!")
        receberProfundidade()
    return prof

def BemVindo():
    print(colored('Oláa, seja muito bem vindo ao meu jogo da velha!!!!!!', 'magenta'))
    print(colored('Aqui vai algumas instruções:','magenta'))
    print(colored('Para jogar você deve escolher as posições desse modo:\n','magenta'))
    board = {
        1: '1', 2: '2', 3: '3',
        4: '4', 5: '5', 6: '6',
        7: '7', 8: '8', 9: '9'
    }
    libs.verificacoes.printTabuleiro(board)
