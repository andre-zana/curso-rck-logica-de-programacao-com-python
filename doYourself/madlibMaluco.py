print('Olá. Bora comigo jogar um jogo comigo?')
print('Ele se chama Madlib, e nele vamos criar uma história maluca!')
resposta = input('[s/n]')
print()

if resposta.lower() == 's':
    print("Complete a história com as palavras, conforme o programa solicita!")
    print()
    lugar = input('Digite o nome de um lugar (cidade, estado ou país): ')
    pessoaFamosa = input('Digite o nome de uma pessoa famosa: ')
    objeto = input('Digite um objeto: ')
    cor = input('Digite uma cor: ')
    verbo = input('Digite um verbo no infinitivo (ex.: correr, andar, cantar, pular e etc): ')
    numero = int(input('Digite um número: '))
    adjetivo = input('Digite um adjetivo (triste, feliz, nervoso e etc): ')
    
    print()
        
    print('Um dia eu estava no(a) ' + lugar + ' quando encontrei o(a) ' + pessoaFamosa + ' segurando um(a) ' + objeto, cor + '.')
    print(f'Do nada, o(a) {pessoaFamosa} decidiu {verbo} exatamente {numero} vezes, sem nenhuma explicação.')
    print('Todo mundo no(a) ' + lugar + ' ficou sem acreditar no que estava acontecendo.')
    print('Foi um dia ' + adjetivo + '!')
else:
    print('NÃO?????')
    print('Ok. Sendo assim, até a próxima! Mas lembre-se: caso queira jogar comigo, é só me procurar por aí! 😉😎')