print("******************************************************************")
print("*            Bem vindo ao jogo de ---ADIVINHAÇÕES--- !!!         *")
print("******************************************************************")

numero_secreto      = 42
total_de_tentativas = 3
rodada              = 1

while (rodada <= total_de_tentativas):
    print("\nTentativa {} de {}".format(rodada, total_de_tentativas))
    chute = input("Digite um número (palpite): ")
    chute = int(chute)
    print("\nVocê digitou: {}".format(chute))

    palpite_correto = chute == numero_secreto
    palpite_maior   = chute > numero_secreto
    palpite_menor   = chute < numero_secreto

    if(palpite_correto):
        print("Parabéns, você acertou! \o/")
    else:
        if(palpite_maior):
            print("Que pena, você errou! :(  O seu palpite foi maior do que o número secreto.")
        elif(palpite_menor):
            print("Que pena, você errou! :(  O seu palpite foi menor do que o número secreto.")

    rodada = rodada + 1

print("\n******************************************************************")
print("*                        Fim do jogo !!!                         *")
print("******************************************************************")