from controllers.no import No
import libs.verificacoes
        
#preenche árvore DFS
def preencheArvore(no:No,jogador:str):
    """Preenche a árvore e seus filhos com todas as posibilidades possiveis jogadas existentes, 

    Args:
        no (No): recebe um no pai
        jogador (str): recebe o jogador pode ser 'X' ou 'O'
    """
    for key in no.board.keys():
        #Verifica se existe espaços vazios
        if libs.verificacoes.espacoVazio(no.board,key):
            #Se estiver vazio ele cria um filho 
            filho = No() #Filho do tipo No
            filho.board = no.board.copy() #filho recebe a copia do pai
            filho.board = libs.verificacoes.InserirJogada(filho.board,jogador,key) 
        
            no.listaFilhos.append(filho)
            
            #Troca o jogador               
            if jogador == "X":
                proximo_jogador = "O"
            else:
                proximo_jogador = "X"
            #Chama recursivamente a função de preencheArvore
            preencheArvore(filho,proximo_jogador)
    
def MinMax(no:No,jogador:str) -> int:
    """Função preenche o minmax, e analisa qual as jogadas possíveis de ganhar.

    Args:
        no (No): recebe um no 
        jogador (string): jogador

    Returns:
        int: retorna o valor do MinMax ou 
        seja atribui 1 - Máquina Ganhar | 2 - Usuário Ganhar | 0 - Empate
    """
    ganhador = libs.verificacoes.checkGanhador(no.board)
    
    if ganhador != ' ':
        #máquina
        if ganhador == 'X':
            no.valorMinMax = 1
            no.listaFilhos = []
            return 1
        
        #Jogador 
        elif ganhador == 'O':
            # print("Entrou aqui O")
            no.valorMinMax = -1
            no.listaFilhos = []
            return -1
        
        #Velha
        elif ganhador == '-':
            # print("Entrou aqui")
            no.valorMinMax = 0
            no.listaFilhos = []
            return 0
        
    #Se ainda não tiver um ganhador
    else:
        if jogador == 'X': #Máquina Maximizar
            for i in range(len(no.listaFilhos)):
                valor = MinMax(no.listaFilhos[i],'O')
                if valor > no.valorMinMax:
                    no.valorMinMax = valor
            return no.valorMinMax
        else:
            no.valorMinMax = 2
            for i in range(len(no.listaFilhos)):
                valor = MinMax(no.listaFilhos[i],'X')
                # print (valor)
                if valor < no.valorMinMax:
                    no.valorMinMax = valor
            return no.valorMinMax
            
