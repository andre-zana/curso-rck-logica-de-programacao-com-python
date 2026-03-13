estudantes = { # A variável 'estudantes' é um dicionário
    1: {'nome': 'André', 'idade': 31, 'curso': 'ADS'},
    2: {'nome': 'Luis', 'idade': 15, 'curso': 'Marketing'},
    3: {'nome': 'Carlos', 'idade': 20, 'curso': 'Direito'},
    4: {'nome': 'Luana', 'idade': 30, 'curso': 'Marketing'}
}

cursos = {'ADS', 'Marketing', 'Direito', 'História'} # A variável 'cursos' é um conjunto

estudantes_cursos = { # A variável 'estudantes_cursos' é um dicionário onde dentro, cada elemento é um conjunto
    'ADS': {1},
    'Marketing': {2, 4},
    'Direito': {3}
}

def addEstudantes(matricula, nome, idade, curso):
    pessoa = {'nome': nome, 'idade': idade, 'curso': curso}
    estudantes[matricula] = pessoa
    if curso not in estudantes_cursos:
        estudantes_cursos[curso] = set()
    estudantes_cursos[curso].add(matricula)

print(estudantes_cursos)
print()
addEstudantes(5, 'Jéssica', 35, 'ADS')
print(estudantes_cursos)
addEstudantes(6, 'João', 35, 'História')
print(estudantes_cursos)
print()
print(estudantes)