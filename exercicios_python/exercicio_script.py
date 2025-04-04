import os

def pedir_idade ():
    """
    Essa função pede ao usuário que digite sua idade.
    Returns:
        int: idade do usuário como int
    """
    while True:
        try:
            """Guarda input do usuário na variavel idade e como é uma string colocamos int"""
            idade = int(input("Digite aqui sua idade: "))
        except ValueError:
            print("Por favor digite apenas Números")
        else:
            print("Idade: ", idade)
            break
    return idade

def pedir_escolha ():
    """
    Essa função pede ao usuário que faça uma escolha.
    Returns:
        int: escolha do usuário como int
    """
    while True:
        try:
            escolha = int(input("Por favor digite um numero de 0 a 3: "))
        except ValueError:
            print("Por favor digite apenas Números")
        else:
            break
    return escolha

def pedir_nome ():
    """
    Essa função pede ao usuário que digite seu nome.
    Returns:
        str: nome do usuario limitado a 48 caracteres como string
    """
    while True:
        nome = input("Digite o Nome: ").strip()
        if len(nome) == 0:
            """se o nome for = a 0 ele vai imprimir para que o usuário digite novamente"""
            print("Por favor digite seu nome")
        elif len(nome) > 48:
            """se o nome for maior que 48 caracters ele vai imprimir que o limite foi atingido"""
            print("Limite de caracteres atingido")
        else:
            break
    return nome

def pedir_altura ():
    """
    Essa função pede ao usuário que digite sua Altura.
    Returns:
        float: altura é decimal portanto utilizamos float
    """
    while True:
        try:
            altura = float(input("Digite aqui sua Altura: "))
        except ValueError:
            print("Por favor digite apenas Números")
        else:
            break
    return altura

def validar (nome, idade, altura):
    """
    Essa função é apenas validação das demais funções
    Returns:
        bool: validar é para retornar caso dê = a 0 ou maior que 48 caracteres como falso
e menor que 0 também.
    """
    ret = True
    if len(nome) == 0:
        ret = False
    elif len(nome) > 48:
        ret = False
    if idade < 0:
        ret = False
    if altura < 0:
        ret = False
    return ret

escolha = -1
nome = ""
idade = -1
altura = -1.0

while True:
    """Esse é um menu para que o usuário consiga escolher a opção desejada:"""
    print("BEM VINDO AO CADASTRO, SELECIONE A OPÇÃO DESEJADA:")
    print("1 - Nome")
    print("2 - Idade")
    print("3 - Altura")
    print("0 - Sair")
    escolha = pedir_escolha()

    match escolha:
        case 0:
            break
        case 1:
            nome = pedir_nome()
        case 2:
            idade = pedir_idade()
        case 3:
            altura = pedir_altura()
        case _:
            print("Opção invalida")
    os.system('cls' if os.name == 'nt' else 'clear')
    if validar(nome, idade, altura):
        print("Nome: ", nome)
        print("Idade: ", idade)
        print("Altura: ", altura)
        break

"""todo: usuário está podendo entrar com idade e altura negativa, não esquecer de arrumar"""