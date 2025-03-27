#Com o Loop for imprima os valores de 1 a 20 e com o Loop While imprima os valores de 20 a 1

for numero in range(1 , 21):
    print(numero)

while numero > 0:
    print(numero)
    numero = numero - 1

gatos = [ "Toninha", "Bisnaga", "Twix", "Churros", "Brioche", "Chihiro", "Lichia"]
print("Quantidade de gatos: ", len(gatos))
for nome in gatos:
    print("O Nome do gato é: ", nome)