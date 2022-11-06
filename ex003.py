'''
3. Faça um Programa que leia 4 notas, mostre as notas e a média.
'''

print("\nDigite as 4 notas bimestrais: ")
n = [0, 0, 0, 0]
n [0] = float(input("\nPrimeira Nota: "))
n [1] = float(input("\nSegunda Nota: "))
n [2] = float(input("\nTerceira Nota: "))
n [3] = float(input("\nQuarta Nota: "))

media = (n[0] + n[1] + n[2] + n[3]) / 4
print('1° Nota - ',n[0])
print('2° Nota - ',n[1])
print('3° Nota - ',n[2])
print('4° Nota - ',n[3])
print("\n" ,media)