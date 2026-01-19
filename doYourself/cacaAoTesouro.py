tabuleiro = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

linhaTesouro = 0
colunaTesouro = 1

def exibirTabuleiro():
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 7) # print('--------')

tentativas = 5

print("🚀 Caça ao Tesouro Espacial")
print()
print("Encontre o 💎 escondido no tabuleiro.")
print("Digite números entre 0 e 2 para linhas e colunas!")
print("Exemplo: Linha 2, coluna 1")
exibirTabuleiro()

for i in range(tentativas):
    print(f"\nTentativa {i+1} de {tentativas}!")
    
    linha = int(input('Digite a linha que deseja (0 à 2): '))
    coluna = int(input('Digite a coluna que deseja (0 à 2): '))
    
    if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
        print('Posição inválida! Por favor, escolha valores entre 0 e 2.')
        continue
    
    if linha == linhaTesouro and coluna == colunaTesouro:
        tabuleiro[linha][coluna] = '💎'
        print("PARABÉNS... Você encontrou o tesouro!!")
        exibirTabuleiro()
        break
    else:
        if tabuleiro[linha][coluna] != ' ':
            print("Você já tentou aqui!")
        else:
            tabuleiro[linha][coluna] = 'X'
            print("O tesouro não está aqui! Continue procurando.")
            exibirTabuleiro()
else:
    print("Suas tentativas chegaram ao fim. Você perdeu!!")
    tabuleiro[linhaTesouro][colunaTesouro] = '💎'
    print("O tesouro estava aqui...")
    exibirTabuleiro()
        
    
    