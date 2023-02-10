import random
from unittest import case
def define_palavra():
    palavras = []
    with open("Frutas.txt") as arquivo:
        conteudo = arquivo.read()
        for linha in conteudo:
            linha = linha.strip()
            print(linha)
            palavras.append(linha)
        arquivo.close()    
    index = random.randint(0, len(palavras))
    palavra_secreta = palavras[index]
    return str(palavra_secreta)

def define_nivel():
    print("Em qual nível você deseja jogar?")
    print("(1)Fácil  (2)Médio  (3)Difícil")
    nivel = int(input("Insira o número:"))
    if nivel == 1:
        max_erros = 7
    elif nivel == 2:
        max_erros = 5
    else:
        max_erros = 3
    return max_erros

def testa_encerra(pAcertos, pQtd_letras, pErros, pMax_erros):
    if (pAcertos == pQtd_letras) and (pErros < pMax_erros):
        encerra = True
    elif (pAcertos < pQtd_letras) and (pErros == pMax_erros):
        encerra = True
    else: 
        encerra = False
    return encerra

def testa_perdeu(pAcertos, pQtd_letras, pErros, pMax_erros):
    if (pAcertos < pQtd_letras) and (pErros >= pMax_erros):
        perdeu = True
    else:
        perdeu = False
    return perdeu

def mostra_forca(pMax_erros, pErros):
    if pMax_erros == 7:
        if pErros == 1: 
            print(" _________")  
            print("|         |")
            print("|        _|_")
            print("|       (   )")
            print("|")
            print("|")
            print("|")
            print("|")
        elif pErros == 2:
            print(" _________")  
            print("|         |")
            print("|        _|_")
            print("|       (x x)")
            print("|")
            print("|")
            print("|")
            print("|")
        elif pErros == 3:
            print(" _________")  
            print("|         |")
            print("|        _|_")
            print("|       (x_x)")
            print("|")
            print("|")
            print("|")
            print("|")
        elif pErros == 4:
            print(" _________")  
            print("|         |")
            print("|        _|_")
            print("|       (x_x)")
            print("|        [ ]")
            print("|")
            print("|")
            print("|")
        elif pErros == 5:
            print(" _________")  
            print("|         |")
            print("|        _|_")
            print("|       (x_x)")
            print("|       |[ ]|")
            print("|")
            print("|")
            print("|")
        elif pErros == 6:
            print(" _________")  
            print("|         |")
            print("|        _|_")
            print("|       (x_x)")
            print("|       |[ ]|")
            print("|        [ ]")
            print("|")
            print("|")
        elif pErros == 7:
            print(" _________")  
            print("|         |")
            print("|        _|_")
            print("|       (x_x)")
            print("|       |[ ]|")
            print("|        [ ]")
            print("|        | |")
            print("|")
        else:
            print(" _________")  
            print("|         |")
            print("|         |")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")

    elif pMax_erros == 5:
        if pErros == 1:
            print(" _________")  
            print("|         |")
            print("|        _|_")
            print("|       (x_x)")
            print("|")
            print("|")
            print("|")
            print("|")
        elif pErros == 1:
            print(" _________")  
            print("|         |")
            print("|        _|_")
            print("|       (x_x)")
            print("|        [ ]")
            print("|")
            print("|")
            print("|")
        elif pErros == 3:
            print(" _________")  
            print("|         |")
            print("|        _|_")
            print("|       (x x)")
            print("|       |[ ]|")
            print("|")
            print("|")
            print("|")
        elif pErros == 4:
            print(" _________")  
            print("|         |")
            print("|        _|_")
            print("|       (x x)")
            print("|       |[ ]|")
            print("|        [ ]")
            print("|")
            print("|")
        elif pErros == 5:
            print(" _________")  
            print("|         |")
            print("|        _|_")
            print("|       (x x)")
            print("|       |[ ]|")
            print("|        [ ]")
            print("|        | |")
            print("|")
        else:
            print(" _________")  
            print("|         |")
            print("|         |")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")

    else:
        if pErros == 1:
            print(" _________")  
            print("|         |")
            print("|        _|_")
            print("|       (x_x)")
            print("|")
            print("|")
            print("|")
            print("|")
        elif pErros == 2:
            print(" _________")  
            print("|         |")
            print("|        _|_")
            print("|       (x x)")
            print("|       |[ ]|")
            print("|")
            print("|")
            print("|")
        elif pErros == 3:
            print(" _________")  
            print("|         |")
            print("|        _|_")
            print("|       (x x)")
            print("|       |[ ]|")
            print("|        [ ]")
            print("|        | |")
            print("|")
        else:
            print(" _________")  
            print("|         |")
            print("|         |")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")

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

    
    perdeu = False
    encerra = False
    pontos = 1000
    erros = 0
    acertos = 0
    max_erros = define_nivel()
    
    palavra_secreta = define_palavra()
    qtd_letras = len(palavra_secreta)
    valores = []
    letras_usadas = set()
    for r in palavra_secreta:
        valores.append("_")

    while (not encerra):
        chute = input("Digite uma letra:")
        chute = chute.strip()
        chute = chute.upper()
        if chute in letras_usadas:
            print("Você já chutou esta letra. Tente outra.")
            print("Letras usadas:")
            print(letras_usadas)
            continue
        else:
            letras_usadas.add(chute)
            print("Letras usadas:")
            print(letras_usadas)
        index = 0
        encontrou = False
        for letra in palavra_secreta:
            if chute == letra.upper():
                encontrou = True
                valores[index] = chute
                acertos += 1 
            index += 1
        if not encontrou:
            print("Não encontrei esta letra")
            erros +=1
        mostra_forca(max_erros, erros)
        mostra_palavra(qtd_letras,valores)
        encerra = testa_encerra(acertos, qtd_letras, erros, max_erros)
        perdeu = testa_perdeu(acertos, qtd_letras, erros, max_erros)
    if perdeu:
        print("Você perdeu!")
    else:
        print("Você ganhou!")
    print("Fim do jogo!")

if (__name__ == "__main__"):
    jogar()