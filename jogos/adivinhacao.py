print("******************************************************************")
print("*            Bem vindo ao jogo de ---ADIVINHAÇÕES--- !!!         *")
print("******************************************************************")
print("")

numero_secreto = 42

chute = input("Digite um número (palpite): ")

print("")

print("Você digitou:", chute, sep=" ")

if(numero_secreto == int(chute)):
    print("Parabéns, você acertou! \o/")
else:
    print("Que pena, você errou! :(")
    print("O número correto era:", numero_secreto)

print("")
print("Fim do jogo.")