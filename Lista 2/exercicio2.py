def substituir_letra(frase, letra_original, letra_substituta):
    nova_frase = frase.replace(letra_original, letra_substituta)
    return nova_frase

frase = input("Digite a frase: ")
letra_original = input("Digite a letra original: ")
letra_substituta = input("Digite a letra substituta: ")

nova_frase = substituir_letra(frase, letra_original, letra_substituta)
print(f"Frase original: {frase}")
print(f"Frase após substituição: {nova_frase}")
