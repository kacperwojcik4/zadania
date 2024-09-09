def nwd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))

wynik = nwd(liczba1, liczba2)

print(f"Największy wspólny dzielnik liczb {liczba1} i {liczba2} to: {wynik}")
