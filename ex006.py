
'''
6. Desenvolva um jogo de acerte o número, onde o computador escolhe um número
inteiro aleatório de 0 a 20, e o usuário tem 5 tentativas para adivinhar o número
'''
import random

print("\nTente acertar um número de 0 a 20")
jogarNovamente = 0

while(jogarNovamente == 0):
    n = random.randint(0,20)
    chance = 0

    while (chance < 5 ):
        chance += 1
        chute = int(input("Qual seu palpite: "))

        if(chute > n):
            print("\nErrou!\nÉ um número menor")
        elif(chute < n):
            print("\nErrou!\nÉ um número maior")
        else:
            print("\nParabéns!!\nVocê acertou com",chance,"tentativas!")
            print("\nQuer jogar novamente?\n")
            escolha = int(input("0 - SIM | 1 - NÃO\n"))
            
            if(escolha == 1):
                jogarNovamente += 1
            else:
                break

            break
    