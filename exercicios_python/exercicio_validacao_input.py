#Crie um script que aceite a entrada do usuário com 1 número, e se ele não digitar número mostrar erro
#e pedir para digitar novamente

while True:
    try:
        numero = int(input("Digite um número: "))
    except ValueError:
        print("Por favor digite apenas Números")
    else:
        print("Seu número é: " , numero)
        break