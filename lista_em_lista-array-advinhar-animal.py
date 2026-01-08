perguntas = [  
    ['Seu animal gosta de bananas?', 'Macaco'],
    ['Seu animal é laranja?', 'Tigre'],
    ['Seu animal vive na água?', 'Peixe'],
    ['Seu animal rasteja?', 'Cobra']
]

while True:
    print("Pense em um animal...")

    acertou = False
    for pergunta in perguntas:
        resposta = input(f'{pergunta[0]} (s/n): ')
        if resposta.lower() == 's':
            print(f'Você pensou em {pergunta[1]}!')
            acertou = True
            break

    if not acertou:
        animal = input('Desisito! Em qual animal você pensou? ')
        novapergunta = input('Qual pergunta você faria sobre o seu animal, para alguém advinhar? ')
        perguntas.append([novapergunta, animal])
    
    resposta = input('Quer jogar novamente (s/n): ')
    if resposta.lower() != 's':
        print('Ok. Foi bom jogar com você!')
        break