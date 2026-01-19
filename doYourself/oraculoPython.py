print('Olá. Bem vindo ao Oráculo da sabedoria Python!')
print()
pergunta = input('Sobre qual tema no Python deseja estudar (Variáveis, Condicional ou Funções? ').lower()

match pergunta:
    case 'variável' | 'variavel' | 'variáveis' | 'variaveis':
        print('Uma variável em Python é um espaço na memória usado para armazenar um valor, como números,')
        print('textos ou listas, que pode ser reutilizado ao longo do programa.')
    case 'condicional' | 'if/else' | 'if' | 'else':
        print('O if é usado para verificar uma condição e executar um código quando ela é verdadeira.')
        print('O else executa outro código quando a condição é falsa.')
    case 'função' | 'funcao' | 'funcão' | 'funçao' | 'funções' | 'funcoes' | 'funçoes' | 'funcões':
        print('Uma função é um bloco de código reutilizável que executa uma tarefa específica.')
        print('Ela ajuda a organizar o programa, evitar repetição de código e facilitar a manutenção.')
    case _:
        print('Desculpe, mas eu ainda estou aprendendo sobre este tema. Volte mais tarde!')