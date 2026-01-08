print("Olá. Eu sou sua IA. O que deseja fazer?")

comando = input('Digite o seu comando: ')

match comando:
    case 'oi' | 'ola' | 'olá':
        print("Olá.")
    case 'tudo bem' | 'bem' | 'como vai' | 'e ai':
        print("Tudo bem e com você?")
    case 'piada' | 'me faça rir' | 'diga algo engraçado':
        print("Por que o livro de matemática estava triste? Porque tinha muitos problemas.")
    case 'sair' | 'tchau' | 'adeus':
        print("Tchau. Até logo!")
    case _:
        print("Desculpe, mas não entendi o comando!")