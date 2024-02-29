def is_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def encontrar_primos_na_lista(lista):
    primos = [numero for numero in lista if is_primo(numero)]
    return primos

lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primos_encontrados = encontrar_primos_na_lista(lista_de_numeros)

print(f"Números primos na lista: {primos_encontrados}")
