#Crie um script que aceita a entrada do usuário de 2 números, mostre a soma dos números
# para o usuário e diga se o resultado é par ou impar
#Input e If

numero = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

soma = numero + numero2
print("O valor da soma é: " , soma)

if soma % 2 == 0:
    print("O resultado é PAR!")
else:
    print("O resultado é IMPAR!")
