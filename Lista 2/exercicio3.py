def contar_palavras(frase):
    palavras = frase.split()  
    return len(palavras)

frase_exemplo = input("Digite uma frase:")
num_palavras = contar_palavras(frase_exemplo)

print(f"A frase '{frase_exemplo}' tem {num_palavras} palavras.")
