print("******************************************************************")
print("*            Bem vindo ao jogo de ---ADIVINHAÇÕES--- !!!         *")
print("******************************************************************")

numero_secreto      = 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print(f"\nTentativa {rodada} de {total_de_tentativas}")
    chute = input("Digite um número (palpite) entre 1 e 100: ")
    chute = int(chute)
    print("\nVocê digitou: {}".format(chute))

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!!!")
        continue

    palpite_correto = chute == numero_secreto
    palpite_maior   = chute > numero_secreto
    palpite_menor   = chute < numero_secreto

    if(palpite_correto):
        print("Parabéns, você acertou! \o/")
        break
    else:
        if(palpite_maior):
            print("Que pena, você errou! :(  O seu palpite foi maior do que o número secreto.")
        elif(palpite_menor):
            print("Que pena, você errou! :(  O seu palpite foi menor do que o número secreto.")

    rodada = rodada + 1

print("\n******************************************************************")
print("*                        Fim do jogo !!!                         *")
print("******************************************************************")