animal1 = "gato"
animal2 = "cachorro"
animal3 = "coelho"
print("Escolha um animal: ")
print("1 - " , animal1)
print("2 - " , animal2)
print("3 - ", animal3)

escolha = -1
while True:
    try:
        escolha = int(input("Digite um número de 1 a 3: "))
    except ValueError:
        print("Por favor digite apenas os animais listados")
    else:
        if escolha < 1 or escolha > 3:
            print("Por favor digite apenas os animais listados!")
        else:
            print("O animal que você escolheu é: " , escolha)
            match escolha:
                case 1:
                    print("GATO")
                case 2:
                    print("CACHORRO")
                case 3:
                    print("COELHO")
                case _:
                    print("Erro Critico")
            break