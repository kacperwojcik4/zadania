import random

lista_liczb = [random.randint(1, 100) for i in range(15)]

najwieksza = max(lista_liczb)
najmniejsza = min(lista_liczb)

print(f"Lista wygenerowanych liczb: {lista_liczb}")
print(f"Największa liczba: {najwieksza}")
print(f"Najmniejsza liczba: {najmniejsza}")
