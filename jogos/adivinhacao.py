# Importação do módulo que gera números aleatórios.
import random

print("******************************************************************")
print("*            Bem vindo ao jogo de ---ADIVINHAÇÕES--- !!!         *")
print("******************************************************************")

# Geração do número aleatório; a função random() gera números entre 1 e 101-1.
numero_secreto = round(random.randrange(1, 101))

# Quantidade máxima de tentativas/palpites no jogo.
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print(f"\nTentativa {rodada} de {total_de_tentativas}")
    chute = input("Digite um número (palpite) entre 1 e 100: ")
    chute = int(chute)
    print(f"\nVocê digitou: {chute}")

    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100!!!")
        continue

    palpite_correto = chute == numero_secreto
    palpite_maior = chute > numero_secreto
    palpite_menor = chute < numero_secreto

    if palpite_correto:
        print("Parabéns, você acertou! :)")
        break
    else:
        if palpite_maior:
            print("Que pena, você errou! :(  O seu palpite foi maior do que o número secreto.")
        elif palpite_menor:
            print("Que pena, você errou! :(  O seu palpite foi menor do que o número secreto.")

    # Se o jogador errar todas as tentativas/palpites, informa qual era o número secreto;
    if rodada == total_de_tentativas and not palpite_correto:
        print(f"\nO número secreto era: {numero_secreto}")

    rodada = rodada + 1

print("\n******************************************************************")
print("*                        Fim do jogo !!!                         *")
print("******************************************************************")
