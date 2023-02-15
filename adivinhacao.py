import random
def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randint(1,101)
    pontos = 1000
    tentativas = 1
    print("Em qual nível você deseja jogar?")
    print("(1)Fácil  (2)Médio  (3)Difícil")
    nivel = int(input("Insira o número:"))

    if nivel == 1:
        chances = 15
    elif nivel == 2:
        chances = 10
    else:
        chances = 5
    while tentativas <= chances:
        print("Você deve colocar um número de 1 a 100")
        chute = int(input("Digite um número:"))
        igual = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        if (chute < 1) or (chute > 100):
            continue
        if igual:
            print("Parabéns! Você acertou em {} tentativa(s)! E fez {} pontos!".format(tentativas, pontos))
            break
        elif maior:
            print("Chute maior do que o número correto.")
        elif menor:
            print("Chute menor do que o número correto.")
        pontos_perdidos = abs(numero_secreto-chute)
        pontos -= pontos_perdidos
        tentativas += 1

    print("Fim do jogo")
    
if (__name__ == "__main__"):
    jogar()