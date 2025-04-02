#Fazer uma função que receba 2 numeros inteiros e retorne a soma
def somar_numeros(numero1, numero2):
    soma = numero1+numero2
    return soma

def printar_string(exercicios):
    print(exercicios)

def hello_world():
    print("Hello World")

def usuario_digita(prompt):
    return input(prompt)

printar_string("Python")

hello_world()

print(somar_numeros(5,6))

print(somar_numeros(7,9))

print(somar_numeros(7,8))

print(usuario_digita("Digite aqui: \n"))