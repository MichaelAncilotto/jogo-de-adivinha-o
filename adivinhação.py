import random

while True:
    tentativas = 0
    limite_tentativas = 3
    numero_computador = (random.randint(1, 5))

    while True:
        print("Qual o Número?")
        resposta = int(input())
        tentativas += 1

        if resposta == numero_computador:
            print(f"Você acertou em {tentativas} tentativas!")
            break

        if tentativas >= limite_tentativas:
            print("Suas tentativas acabaram!")
            break

        elif resposta < numero_computador:
            print("Tá baixo!")

        elif resposta > numero_computador:
            print("Tá alto!")

    if tentativas >= limite_tentativas or resposta == numero_computador:
        replay = input("Quer jogar denovo? Sim/Não")
        if replay == ("Não"):
            break
