import random
numero_computador = (random.randint(1, 5))

while True:
    print("Qual o número?")
    resposta = int(input())
    if resposta == numero_computador:
        print("Você acertou!")
    else:
        print("Você errrou")
    if resposta == numero_computador:
        break
