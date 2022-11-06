'''
4. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
'''

n = 50
i = 0
while (i < 50):
    (n%2 == 0)  or print('\n',n)
    n -= 1
    i += 1

#ou assim

""" while (i < 50):
    if (n%2 == 0):      # PAR
        n -= 1
    else:
        print('\n',n)
        n -= 1
    
    i += 1 """