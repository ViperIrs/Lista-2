def encontrar_pares_soma(lista, valor_soma):
    pares = []

    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == valor_soma:
                pares.append((lista[i], lista[j]))

    return pares

minha_lista = [1, 2, 3, 4, 5, 6]
valor_alvo = 7

pares_encontrados = encontrar_pares_soma(minha_lista, valor_alvo)

if pares_encontrados:
    print(f"Pares cuja soma é {valor_alvo}: {pares_encontrados}")
else:
    print(f"Não foram encontrados pares cuja soma é {valor_alvo}.")
