'''
1. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha
igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as
informações.
'''

user = input("\nDigite seu usuário: ").lower()
senha = input("Agora digite a sua senha: ").lower()

while (user == senha):
    print("\nDesculpe!\nNome de Usuário e Senha não podem possuir o mesmo valor\n")
    user = input("Digite novamente seu username: ").lower()
    senha = input("Agora sua senha: ").lower()
else:
    print("\n--Maravilha! Você foi cadastrada(o)!--\n")


