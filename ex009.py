
'''
9. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um
crime. As perguntas são:
i) "Telefonou para a vítima?"
ii) "Esteve no local do crime?"
iii) "Mora perto da vítima?"
iv) "Devia para a vítima?"
v) "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
--> Se a pessoa responder positivamente a 2 questões ela deve ser classificada como --> &quot;Suspeita&quot;,
--> entre 3 e 4 como --> &quot;Cúmplice&quot;
--> e 5 como --> &quot;Assassino&quot;.
--> Caso contrário, ele será classificado como --> &quot;Inocente&quot;.
'''

perguntas = ['Telefonou para a Vítima?', 'Esteve no local do Crime?', 'Mora perto da Vítima?', 'Devia para a Vítima?', 'Ja trabalhou com a Vítima?']
res = 0
c = 0

while(c < 5):
  print("-"*20)
  print('\n',perguntas[c])
  n = int(input(print("Digite 1 - SIM | 0 - NÃO")))
  
  if(n == 1): res += 1

  c += 1

if(res == 5): print("O(a) Interrogado(a) é o(a) Assassino(a)!!!")
elif(res == 4 or res == 3): print("O(a) Interrogado(a) é um(a) Cúmplice!")
elif(res == 2): print("O(a) Interrogado(a) é um(a) Suspeito(a).")
else: print("Inocente.!.")



# ou assim

'''
res = ['a' , 'b' , 'c' , 'd' , 'e']
print("Olá serão feitas algumas perguntas sobre o caso e gostaria que você respondesse com sinceridade!\n")
print("Responda somente:\n S - SIM | N - NÃO    \n")
res[0] = str(input("1° - Telefonou para a Vítima no dia do crime?\n>"))
res[0] = res[0].upper()

res[1] = str(input("2° - Esteve no local do crime?\n>"))
res[1] = res[1].upper()

res[2] = str(input("3° - Mora perto da vítima?\n>"))
res[2] = res[2].upper()

res[3] = str(input("4° - Devia dinheiro para a vítima?\n>"))
res[3] = res[3].upper()

res[4] = str(input("5° - 5: Já trabalhou com a vítima?\n>"))
res[4] = res[4].upper()

#-----

if res[0] == "S":
  if res[1] == "S":
    if res[2] == "S":
      if res[3] == "S":
        if res[4] == "S":                                    #-------[S=5|N=0]
          print("O(a) interrogato(a) é o Assassino!!!")
        elif res[4] == "N":                                  #-------[S=4|N=1]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
      
      elif res[3] == "N":  #--D -> nao
        if res[4] == "S":                                    #-------[S=4|N=1]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
        elif res[4] == "N":                                  #-------[S=3|N=2]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
          
    elif res[2] == "N":  #--C -> nao
      if res[3] == "S":
        if res[4] == "S":                                    #-------[S=4|N=1]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
        elif res[4] == "N":                                  #-------[S=3|N=2]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
      
      elif res[3] == "N":
        if res[4] == "S":                                    #-------[S=3|N=2]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
        elif res[4] == "N":                                  #-------[S=2|N=3]
          print("O(a) interrogado(a) é Suspeito(a).")

  elif res[1] == "N":  #--B -> nao
    if res[2] == "S":
      if res[3] == "S":
        if res[4] == "S":                                    #-------[S=4|N=1]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
        elif res[4] == "N":                                  #-------[S=3|N=2]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
      
      elif res[3] == "N":  #--D -> nao
        if res[4] == "S":                                    #-------[S=3|N=2]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
        elif res[4] == "N":                                  #-------[S=2|N=3]
          print("O(a) interrogado(a) é Suspeito(a).")
          
    elif res[2] == "N":  #--C -> nao
      if res[3] == "S":
        if res[4] == "S":                                    #-------[S=3|N=2]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
        elif res[4] == "N":                                  #-------[S=2|N=3]
          print("O(a) interrogado(a) é Suspeito(a).")
      
      elif res[3] == "N":
        if res[4] == "S":                                    #-------[S=2|N=3]
          print("O(a) interrogado(a) é Suspeito(a).")
        elif res[4] == "N":                                  #-------[S=1|N=4]
          print("O(a) interrogado(a) é Inocente")

elif res[0] == "N":  #--A -> nao
  if res[1] == "S":
    if res[2] == "S":
      if res[3] == "S":
        if res[4] == "S":                                   #-------[S=4|N=1]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
        elif res[4] == "N":                                  #-------[S=3|N=2]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
      
      elif res[3] == "N":  #--D -> nao
        if res[4] == "S":                                    #-------[S=3|N=2]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
        elif res[4] == "N":                                  #-------[S=2|N=3]
          print("O(a) interrogado(a) é Suspeito(a).")
          
    elif res[2] == "N":  #--C -> nao
      if res[3] == "S":
        if res[4] == "S":                                    #-------[S=3|N=2]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
        elif res[4] == "N":                                  #-------[S=2|N=3]
          print("O(a) interrogado(a) é Suspeito(a).")
      
      elif res[3] == "N":
        if res[4] == "S":                                    #-------[S=2|N=3]
          print("O(a) interrogado(a) é Suspeito(a).")
        elif res[4] == "N":                                  #-------[S=1|N=4]
          print("O(a) interrogado(a) é Inocente")

  elif res[1] == "N":  #--B -> nao
    if res[2] == "S":
      if res[3] == "S":
        if res[4] == "S":                                    #-------[S=3|N=2]
          print("O(a) interrogado(a) é um(a) Cúmplice!")
        elif res[4] == "N":                                  #-------[S=2|N=3]
          print("O(a) interrogado(a) é Suspeito(a).")
      
      elif res[3] == "N":  #--D -> nao
        if res[4] == "S":                                    #-------[S=2|N=3]
          print("O(a) interrogado(a) é Suspeito(a).")
        elif res[4] == "N":                                  #-------[S=1|N=4]
          print("O(a) interrogado(a) é Inocente")
          
    elif res[2] == "N":  #--C -> nao
      if res[3] == "S":
        if res[4] == "S":                                    #-------[S=2|N=3]
          print("O(a) interrogado(a) é Suspeito(a).")
        elif res[4] == "N":                                  #-------[S=1|N=4]
          print("O(a) interrogado(a) é Inocente")
      
      elif res[3] == "N":
        if res[4] == "S":                                    #-------[S=1|N=4]
          print("O(a) interrogado(a) é Inocente")
        elif res[4] == "N":                                  #-------[S=0|N=5]
          print("O(a) interrogado(a) é Inocente")
'''