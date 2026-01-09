notas = [1, 7.5, 10, 9.9]
media = 0

# loop (laço)
# for é a palavra-chave do Python que inicia o laço, indicando ao programa que deseja começar a iterar em um conjunto de dados. 
# abacaxi (variável temporária ou variável de iteração DO LOOP). A variável recebe o valor de cada item da sequência notas em cada iteração, um de cada vez.
# in é a palavra-chave que indica a sequência ou coleção de itens que deseja percorrer.
# notas é uma variável do tipo lista (array), que contém os itens sobre os quais você deseja iterar. Em cada volta do loop, um item de notas será atribuído à variável abacaxi.
for abacaxi in notas:
    media += abacaxi # ou media = media + abacaxi

media /=4 # ou media = media/4

print(f'A média é {media}')