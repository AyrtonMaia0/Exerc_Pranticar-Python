'''
8. Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que
adivinhar uma palavra que será mostrada com as letras embaralhadas.
O programa terá uma lista de palavras previamente definidas e escolherá uma aleatoriamente. 
O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser
mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.
'''
import random

chute = 6
palavras = ['TESTE','PROGRAMA','CUBOMAGICO','JAVASCRIPT','RECNPLAY','PYTHON']
sortear = random.choice(palavras)                                               #Retornar um elemento aleatório de uma lista:
while chute != 0:                                                               #Sempre que 'chute' for diferente de Zero
    embaralhar = random.sample(sortear, len(sortear))                           #vai pegar a palavra - seu tamanho - deixar cada letra da palavra em um campo - embaralhar

    juntarPalavra = ''.join(embaralhar)                                         #Vai juntar as letras que eram listas
    print(juntarPalavra)                                                        #Exibe a palavra embaralhada para o user tentar
    print("-"*20)
    tentativa = input("Digite a palavra: ").upper()
    if tentativa == sortear:
        print("\nParabéns! Você venceu!")
        break
    else:
        chute -= 1
        print("\nVoce errou! Tentativas restantes {chute}")
        print("-"*20)