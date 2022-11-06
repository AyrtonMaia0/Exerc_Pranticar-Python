'''
10. Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se ele é: equilátero, isósceles ou escaleno.
Dicas:
i) Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
ii) Triângulo Equilátero: três lados iguais;
iii) Triângulo Isósceles: quaisquer dois lados iguais;
iv) Triângulo Escaleno: três lados diferentes;
'''

criterio = 0
while (criterio == 0):
  lado1 = int(input("Digite o Primeiro Lado: "))
  lado2 = int(input("Digite o Segundo Lado: "))
  lado3 = int(input("Digite o Terceiro Lado: "))

  if (lado1+lado2 > lado3) and (lado1+lado3 > lado2) and (lado2+lado3 > lado1):
    print(">Isto é um Triângulo!\n")
    
    if (lado1 == lado2 and lado1 == lado3 and lado2 == lado3):
      print("É um Triângulo Equilátero!")
    elif(lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
      print("É um Triângulo Isóceles!")
    elif(lado1 != lado2 and lado1 != lado3 and lado2 != lado3):
      print("É um Triângulo Escaleno!")
    
    print("-"*20)

  else:
    print(">Isto não é um Triângulo!\n")
    print("-"*20)

  jogarNovamente = int(input("Você deseja Continuar? (Sim = 1 ; Não = 0)"))
  
  if(jogarNovamente == 0):
    criterio = 1 #or break  or criterio += 1 """