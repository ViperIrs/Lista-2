def intersecao_listas(lista1, lista2):
    intersecao = []

    for elemento in lista1:
        if elemento in lista2 and elemento not in intersecao:
            intersecao.append(elemento)

    return intersecao


lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]

resultado = intersecao_listas(lista1, lista2)
print(f"A interseção das listas é: {resultado}")
