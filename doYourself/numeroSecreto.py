numeroScreto = 95
tentativas = 0

while True:
    chute = int(input('Tente advinhar o número que estou pensando: '))
    print()
    tentativas = tentativas + 1 # ou tentativas += 1
    if chute == numeroScreto:
        print(f"PARABÉNS... Você acertou em {tentativas} tentativas!")
        break
    else:
        print('Você errou. Por favor, tente novamente!')
        print()