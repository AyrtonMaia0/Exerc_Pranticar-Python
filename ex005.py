'''
5. Faça um programa que leia 5 números e informe o maior número.
'''
print("\nDigite 5 números:")

n = [0, 0, 0, 0, 0]

n[0] = input("Number One: ")
n[1] = input("Number Two: ")
n[2] = input("Number Three: ")
n[3] = input("Number Four: ")
n[4] = input("Number Five: ")

if(n[0]>n[1] and n[0]>n[2] and n[0]>n[3] and n[0]>n[4]):
    print("\nO maior Número é ",n[0])
elif(n[1]>n[2] and n[1]>n[3] and n[1]>n[4]):
    print("\nO maior Número é ",n[1])
elif(n[2]>n[3] and n[2]>n[4]):
    print("\nO maior Número é ",n[2])
elif(n[3]>n[4]):
    print("\nO maior Número é ",n[3])
else:
    print("\nO maior Número é ",n[4])