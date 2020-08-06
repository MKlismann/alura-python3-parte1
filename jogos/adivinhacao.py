print("******************************************************************")
print("*            Bem vindo ao jogo de ---ADIVINHAÇÕES--- !!!         *")
print("******************************************************************")
print("")

numero_secreto = 42

chute = input("Digite um número (palpite): ")
chute = int(chute)

print("")
print("Você digitou:", chute, sep=" ")

palpite_correto = chute == numero_secreto
palpite_maior = chute > numero_secreto
palpite_menor = chute < numero_secreto

if(palpite_correto):
    print("Parabéns, você acertou! \o/")
else:
    if(palpite_maior):
        print("Que pena, você errou! :(  O seu palpite foi maior do que o número secreto.")
    elif(palpite_menor):
        print("Que pena, você errou! :(  O seu palpite foi menor do que o número secreto.")
    print("O número correto era:", numero_secreto)

print("")
print("Fim do jogo.")