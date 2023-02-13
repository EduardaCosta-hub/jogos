import random
import imagens_forca
from unittest import case

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de forca!")
    print("*********************************")

    perdeu = False
    encerra = False
    erros = 0
    acertos = 0
    max_erros = define_nivel()
    palavra_secreta = define_palavra()
    qtd_letras = len(palavra_secreta)
    letras_palavra = define_letras_palavra()
    letras_usadas = set()

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
                letras_palavra[index] = chute
                acertos += 1 
            index += 1
        if not encontrou:
            print("Não encontrei esta letra")
            erros +=1

        mostra_forca(max_erros, erros)
        mostra_palavra(qtd_letras,letras_palavra)
        encerra = testa_encerra(acertos, qtd_letras, erros, max_erros)
        perdeu = testa_perdeu(acertos, qtd_letras, erros, max_erros)
        
    if perdeu:
        print("Você perdeu!")
    else:
        print("Você ganhou!")
    print("Fim do jogo!")

#Funções

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

def define_palavra():
    palavras = []
    with open("Frutas.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
        arquivo.close()    
    #print(palavras)
    index = random.randint(0, len(palavras))
    palavra_secreta = palavras[index]
    return str(palavra_secreta)

def define_letras_palavra(pPalavra_secreta):
    lista = []
    for r in pPalavra_secreta:
        lista.append("_")
    return lista

def mostra_forca(pMax_erros, pErros):
    if pMax_erros == 7:
        case 
        pErros == 0: imagens_forca.img0()
        pErros == 1: imagens_forca.img1()
        pErros == 2: imagens_forca.img2()
        pErros == 3: imagens_forca.img3()
        pErros == 4: imagens_forca.img4()
        pErros == 5: imagens_forca.img5()
        pErros == 6: imagens_forca.img6()
        pErros == 7: imagens_forca.img7()

    elif pMax_erros == 5:
        case 
        pErros == 0: imagens_forca.img0()
        pErros == 1: imagens_forca.img3()
        pErros == 2: imagens_forca.img4()
        pErros == 3: imagens_forca.img5()
        pErros == 4: imagens_forca.img6()
        pErros == 5: imagens_forca.img7()

    else:
        case 
        pErros == 0: imagens_forca.img0()
        pErros == 1: imagens_forca.img3()
        pErros == 2: imagens_forca.img5()
        pErros == 3: imagens_forca.img7()

def mostra_palavra(pQtd_letras,pValores):
    print("Palavra:")
    r = 0
    while r < pQtd_letras:
        print(pValores[r], end="")
        r += 1
    print(" ")

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


if (__name__ == "__main__"):
    jogar()