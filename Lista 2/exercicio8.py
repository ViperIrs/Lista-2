import random

def embaralhar_lista(lista):
    lista_embaralhada = lista.copy()
    random.shuffle(lista_embaralhada)
    return lista_embaralhada

minha_lista = [1, 2, 3, 4, 5]
lista_embaralhada = embaralhar_lista(minha_lista)

print(f"Lista original: {minha_lista}")
print(f"Lista embaralhada: {lista_embaralhada}")
