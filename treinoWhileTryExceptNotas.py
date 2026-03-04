def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_aprovacao(media):
    if media >= 6:
        return "Aprovado"
    else:
        return "Reprovado"

notas = []

while True:
    entrada = input("Digite uma nota (ou ENTER para finalizar): ").strip()
    
    if entrada == "":
        break
    
    try:
        nota = float(entrada)
        if nota >= 0 and nota <= 10: # ou no "estilo Python": if 0 <= nota <= 10: (Está entre 0 e 10 incluindo 0 e 10)
            notas.append(nota)
        else:
            print('Digite notas entre 0 e 10.')
    except ValueError:
        print('Digite um número válido!')

if len(notas) == 0: # ou em boas práticas: if not notas:
    print('Você não digitou nenhuma nota!')
else:
    media = calcular_media(notas)
    print('Quantidade de notas: ',len(notas))
    print('Notas: ', notas)
    print(f'Média: {media:.2f}')
    print('Situação: ', verificar_aprovacao(media))