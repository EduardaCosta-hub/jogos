import forca
import adivinhacao
import os
print("*********************************")
print("*****Olá! Escolha o seu jogo*****")
print("*********************************")
print(os.getcwd())
print("(1)Adivinhação  (2)Forca")
jogo = int(input("Digite o número:"))
if jogo == 1:
    print("Carregando jogo de adivinhação...")
    adivinhacao.jogar()
else:
    print("Carregando jogo de adivinhação...")
    forca.jogar()