soma = 0
n = 1

#--------------------------------------------------------------------------
# ALGUMAS FORMAS DE FAZER
#--------------------------------------------------------------------------

# While: 'Enquanto' n for menor (<) ou igual (=) à 10, será somado, caso seja maior, encerra a somatória.
# While é usado quando eu não sei o nº de vezes que irei repetir.
# while n <= 10:
#     soma = soma + n
#     n = n + 1

    # print(f'Soma: {soma}')
    # print(f'n: {n}')

#--------------------------------------------------------------------------
#--------------------------------------------------------------------------

# For: 'Enquanto' index "qualquer" (variável index - "de tanto até tanto") dentro de um range (intervalo) de 1 até 11, será somado, caso seja maior, encerra a somatória.
# Intervalo aberto (1) e fechado (11), ou seja, vai de 1 até 10, encerrando em 11 (Não segue a somatória no 11, parando em 10) 
# For é usado quando eu sei o nº de vezes que irei repetir.
# for index in range (1,11): # Intervalo fechado ' [ ' e Intervalo aberto ' ) ' -> Na matemática!
    # # print(index) -> a variável index são os números de 1 até 10.
    # soma = soma + n
    # n = n + 1

    # print(f'Soma: {soma}')
    # print(f'n: {n}')

#--------------------------------------------------------------------------
#--------------------------------------------------------------------------

# for index in range (1,11):
    # soma = soma + index # Desta forma, eu não preciso mais de ' n = n + 1 '.

    # print(f'Soma: {soma}')
    # print(f'n: {n}')

#--------------------------------------------------------------------------
#--------------------------------------------------------------------------

for index in range (1,11):
    soma += index # Desta forma, eu não preciso mais de ' n = n + 1 ', e ' soma = soma + index ' pode ser escrito de outras formas.

    print(f'Soma: {soma}')
    print(f'n: {n}')

#--------------------------------------------------------------------------
#--------------------------------------------------------------------------

# Método List Comprehension ou Compreensão de Listas ( nova_lista = [expressao for item in iteravel if condicao] )
# Função sum(...) integrada do Python recebe um iterável (como a lista criada) como argumento e retorna a soma de todos os seus elementos. 
# Ela opera sobre a lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], calcula a soma total (1 + 2 + ... + 10 = 55), e esse valor é atribuído à variável soma. 
# soma = sum([ i for i in range(1,11)])

print()
print(f'A soma dos números de 1 à 10 é {soma}!') # O ' f ' é um tipo de formatação do Python, que formata o tipo do valor. No exercício realizado, está convertendo o tipo de número para o tipo de texto.

