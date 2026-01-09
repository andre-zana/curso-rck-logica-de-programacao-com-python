# def significa defined (definir função)
def olaMundo(): # olaMundo é o nome da função e ela não possui parâmetro
    print('Olá, mundo!')

# olaMundo() # Estou chamando a função.


def olaPessoa(nome): # Existe parâmetro (variável 'nome')
    print(f'Olá, {nome}!')

# olaPessoa('André') # Estou chamando a função e passando um argumento ('André' e 'Luis')
# olaPessoa('Luis')


def dobro(numero): # Existe parâmetro (variável 'numero')
    return numero * 2 # Ele retorna o valor da multiplicação, mas não imprime
    # print(numero * 2) # Ele imprime o valor da multiplicação

# dobro(5) + 3 # Apresenta erro " TypeError: unsupported operand type(s) for +: 'NoneType' and 'int' ", pois não é possível somar diferentes tipos de valores.
# print(dobro(5)) # Ele imprime o valor da multiplicação
# print(dobro(5) + 3) # Ele imprime o valor da multiplicação e depois soma '3'


# def multiplicaDoisNumeros(a, b): # Existe 2 parâmetros (variáveis 'a' e 'b')
#     return a * b # Ele retorna o valor da multiplicação, mas não imprime
    
# print(multiplicaDoisNumeros(5, 3)) # Ele imprime o valor da multiplicação, levando em consiuderação esses 2 argumentos.
# print(multiplicaDoisNumeros(5)) # Apresentara erro relacionado a falta do 2º parâmetro, pois o valor 5 é referente a 'a'. Falta um valor para 'b' (Requerido/Obrigatório).

def multiplicaDoisNumeros(a, b = 8): # Existe 2 parâmetros (variáveis 'a' e 'b') e o 2º parâmetro tem valor já definido ((8) default). NÃO PODE SER NO 1º PARÂMETRO!
    return a * b # Ele retorna o valor da multiplicação, mas não imprime
    
print(multiplicaDoisNumeros(5, 3)) # Ele imprime o valor da multiplicação, levando em consiuderação esses 2 argumentos. Ignora o valor 8 (default) de 'b' no parâmetro.
print(multiplicaDoisNumeros(5)) # 5 é o valor do parâmetro 'a' e ele utiliza 8 (default) para o parâmetro 'b'.


x = 5 # Variável global
def soma():
    x = 10 # Variável local e se não existir variável local, leva em consideração a variável global.
    print(x) # imprime 10, mas eu preciso chamar a função fora do escopo.
    return x + 1 # 'return' Efetua a somatória, mas não imprime, não salva, não usa, não faz nada, além de encerrar a função

print(soma())
# soma() # Chama a função
print(x) # imprime 5