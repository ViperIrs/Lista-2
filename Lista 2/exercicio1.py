def ContarVogais(frase):
    vogais= "aeiouAEIOU"
    contador = 0

    for char in frase:
        if char in vogais:
            contador += 1

    return contador

string = input("Digite o texto:")
num_vogais = ContarVogais(string)
print (num_vogais)
