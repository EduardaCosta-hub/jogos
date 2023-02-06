import random
def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de forca!")
    print("*********************************")

    palavra_secreta = "PARALELEPIPEDO"
    qtd_letras = len(palavra_secreta)
    valores = []
    ganhou = False
    perdeu = False
    pontos = 1000
    tentativas = 1

    print("Em qual nível você deseja jogar?")
    print("(1)Fácil  (2)Médio  (3)Difícil")
    nivel = int(input("Insira o número:"))
    r = 0
    while r < qtd_letras:
        valores.append("_")
        r += 1
    while (not ganhou) and (not perdeu):
        chute = input("Digite uma letra:")
        chute = chute.strip()
        index = 0
        encontrou = False
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                encontrou = True
                valores[index] = chute.lower()
            index += 1
        print("Palavra:")
        r = 0
        resto = 0
        while r < qtd_letras:
            print(valores[r], end='')
            if valores[r] == "_":
                resto +=1
            r += 1
        print("")
        if resto == 0:
            ganhou = True
        if not encontrou:
            print("Não encontrei esta letra")

    print("Fim do jogo!")

if (__name__ == "__main__"):
    jogar()