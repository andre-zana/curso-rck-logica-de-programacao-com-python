# ---------------------------------------------------------------------
tabuleiro = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]
# tabuleiro = [ [ ' ' for _ in range(0, 3)] for _ in range(0, 3) ]
# ---------------------------------------------------------------------

jogador = 'X'

def exibirTabuleiro():
    for linha in tabuleiro:
        print(' |' .join(linha)) # print(f'{linha[0]} |{linha[1]} |{linha[2]}')
        print('-' * 8) # print('--------')

def jogada(linha, coluna):
    if (
        not 0 <= linha <= 2 or
        not 0 <= coluna <= 2 or
        tabuleiro[linha][coluna] != ' '
    ):
        print('Jogada inválida!')
        return jogador
    tabuleiro[linha][coluna] = jogador    
    # ---------------------------------------
    return 'O' if jogador == 'X' else 'X'
    # if jogador == 'X':
    #     return 'O'
    # else:
    #     return 'X'
    # ---------------------------------------

def temGanhador():
    """ Verifica as linhas """ # Tipo de comentário de múltiplas linhas, também chamado de docstring.
    for linha in range(3):
        if (
            tabuleiro[linha][0] != ' ' and
            tabuleiro[linha][0] == tabuleiro[linha][1] and
            tabuleiro[linha][0] == tabuleiro[linha][2]
        ):
            print(f'O jogador {tabuleiro[linha][0]} VENCEU!')
            return True
    
    """ Verifica as colunas """
    for coluna in range (3):
        if (
            tabuleiro[0][coluna] != ' ' and
            tabuleiro[0][coluna] == tabuleiro[1][coluna] and
            tabuleiro[0][coluna] == tabuleiro[2][coluna]
        ):
            print(f'O jogador {tabuleiro[0][coluna]} VENCEU!')
            return True
    
    """ Verifica as diagonais """
        if (
            tabuleiro[1][1] != ' ' and
            (
                (
                    tabuleiro[0][0] == tabuleiro[1][1] and
                    tabuleiro[0][0] == tabuleiro[2][2]
                ) or
                (
                    tabuleiro[0][2] == tabuleiro[1][1] and
                    tabuleiro[1][1] == tabuleiro[2][0]
                )
            )
        ):
            print(f'O jogador {tabuleiro[1][1]} VENCEU!')
            return True
    
    """ Se deu Velha... """
    return False

def temEmpate():
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == ' ':
                return False
    print('Deu Velha!')
    return True
        
while True:
    print(f'Jogador da vez: {jogador}')
    try:
        linha = int(input('Digite a linha que deseja jogar (0 à 2): '))
        coluna = int(input('Digite a coluna que deseja jogar (0 à 2): '))
        jogador = jogada(linha, coluna)
    except IndexError:
        print('Digite valores numéricos de 0 à 2!')
    except ValueError:
        print('Digite valores numéricos inteiros!')
    exibirTabuleiro()
    if temGanhador() or temEmpate():
        break