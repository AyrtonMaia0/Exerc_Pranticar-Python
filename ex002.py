'''
2.  Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
Após isto, calcule a média anual das temperaturas e 
mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram 
(mostrar o mês por extenso: 1 – janeiro, 2 – fevereiro, . . .).
'''


meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro",]
temperaturas = []
for i in range(12):
    temperaturas.append(
        float(input(f"Digite a temperatura de {meses[i]} em ºC: "))
    )

qtdMes = len(meses)

media = sum(temperaturas) / qtdMes
print(f"\nA média das temperaturas foi {media:.2f}ºC\n")
print("-"*30)
print("\nMeses com temperaturas acima da média: ")

for i in range(qtdMes):
    if temperaturas[i] > media:
        print(f"{i+1} - {meses[i].capitalize()} com {temperaturas[i]:.2f}ºC\n")

print("-"*40)
print("FIM\n")




"""
mes = dict()                                                #criacao do dicionario/lista
soma = 0

print("Diga a temperatura média de cada mês:")
mes['Janeiro'] = int(input('Janeiro: '))
mes['Fevereiro'] = int(input('Fevereiro: '))
mes['Março'] = int(input('Março: '))
mes['Abril'] = int(input('Abril: '))
mes['Maio'] = int(input('Maio: '))
mes['Junho'] = int(input('Junho: '))
mes['Julho'] = int(input('Julho: '))
mes['Agosto'] = int(input('Agosto: '))
mes['Setembro'] = int(input('Setembro: '))
mes['Outubro'] = int(input('Outubro: '))
mes['Novembro'] = int(input('Novembro: '))
mes['Dezembro'] = int(input('Dezembro: '))
#print(mes)

for i in mes:                                                   #vai somar os 12 meses
  soma = soma + mes[i]
  
media = soma / len(mes)                                         #descobrir a media dos 12 meses
print(f'A media de temperatura Anual é de: {media:.2f}\n')

print("-"*20)
print('Os meses acima da média Anual são:')

for m, t in mes.items():                                        #m = ao nome do mês | t = a temperatura do mês | (m:t) = (Janeiro:1)
  if t > media:
    print(m, '-', t)
"""