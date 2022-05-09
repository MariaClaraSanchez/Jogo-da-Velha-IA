class No: #(Classe No)
    """ Utilizada para fazer algumas definições e criação de alguns métodos,
    tais como iniciar o tabuleiro, imprimir essa tabuleiro na tela, verificar espaços vazios no tabuleiro
    """
    def __init__(self) -> None:
        """ Iniciação do tabuleiro como um dicionário
        """
 
        ### Na criação do dicionário atribui a chave dele sendo cada posição e cada uma está recebendo um valor vazio e esse valor vai ser o que vou manipular depois
        self.board = {
            1: ' ', 2: ' ', 3: ' ',
            4: ' ', 5: ' ', 6: ' ',
            7: ' ', 8: ' ', 9: ' '
        }
        #preciso de um inteio para o MinMax
        self.valorMinMax = -2
        self.listaFilhos = [] #Lista de filhos do tipo Nó