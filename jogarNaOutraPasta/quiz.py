perguntas = [
    ['Qual animal gosta de bananas?', 'macaco'],
    ['Qual a raiz quadrada de 49?', '7'],
    ['Qual linguagem de programação, o símbolo é uma cobra?', 'python'],
    ['Quanto é 2 + 2?', '4']
]

acertos = 0

for pergunta in perguntas:
    resposta = input(pergunta[0] + " ") # Guarda o que o usuário digitou, na variável RESPOSTA
    if resposta.lower() == pergunta[1]:
        acertos += 1 # ou acertos = acertos + 1

print(f"Você acertou {acertos} de {len(perguntas)} perguntas!")