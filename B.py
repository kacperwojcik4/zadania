def NWD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))

wynik = NWD(liczba1, liczba2)

print(f"Największy wspólny dzielnik liczb {liczba1} i {liczba2} to: {wynik}")
