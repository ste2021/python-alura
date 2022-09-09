import forca
import adivinhacao

print("*********************************")
print("***Escolha seu Jogo!*************")
print("*********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo?"))

if(jogo == 1):
    forca.jogar()
elif(jogo == 2):
    adivinhacao.jogar()
