import random
def define_palavra():
    palavras = ["banana","maçã","morango","melancia","manga"]
    qtd_palavras = len(palavras)
    index = random.randint(0, qtd_palavras)
    palavra_secreta = palavras[index]
    return palavra_secreta
    
def mostra_palavra(pQtd_letras,pValores):
    print("Palavra:")
    r = 0
    while r < pQtd_letras:
        print(pValores[r], end="")
        r += 1
    print(" ")

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de forca!")
    print("*********************************")

    palavra_secreta = define_palavra()
    qtd_letras = len(palavra_secreta)
    valores = []
    perdeu = False
    acertou = False
    pontos = 1000
    tentativas = 1

    print("Em qual nível você deseja jogar?")
    print("(1)Fácil  (2)Médio  (3)Difícil")
    nivel = int(input("Insira o número:"))
    r = 0
    while r < qtd_letras:
        valores.append("_")
        r += 1
    while (not perdeu) and (not acertou):
        chute = input("Digite uma letra:")
        chute = chute.strip()
        index = 0
        encontrou = False
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                encontrou = True
                valores[index] = chute
            index += 1
        if not encontrou:
            print("Não encontrei esta letra")
        mostra_palavra(qtd_letras,valores)
    print("Fim do jogo!")

if (__name__ == "__main__"):
    jogar()