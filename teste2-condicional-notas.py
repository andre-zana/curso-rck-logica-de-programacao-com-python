nota = float(input("Digite a sua nota: "))
print()

if nota >= 7:
    print("Você está de parabéns. APROVADO!")
elif nota >= 5 and nota < 7: # outra forma de escrever esta linha é: ' 4.9elif 5 >= nota < 7: '
    print("Vá para a recuperação e tente novamente!")
else:
    print("Você fracassou. RE PRO VA DO!!!")