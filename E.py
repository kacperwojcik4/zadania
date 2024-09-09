def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def pomnoz(a, b):
    return a * b

def podziel(a, b):
    if b == 0:
        return "Błąd: Dzielenie przez zero!"
    return a // b  # Dzielenie całkowite

def kalkulator():
    print("Prosty Kalkulator")
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")

    wybor = input("Wprowadź wybór (1/2/3/4): ")

    if wybor in ['1', '2', '3', '4']:
        liczba1 = int(input("Podaj pierwszą liczbę całkowitą: "))
        liczba2 = int(input("Podaj drugą liczbę całkowitą: "))

        if wybor == '1':
            print(f"Wynik: {liczba1} + {liczba2} = {dodaj(liczba1, liczba2)}")

        elif wybor == '2':
            print(f"Wynik: {liczba1} - {liczba2} = {odejmij(liczba1, liczba2)}")

        elif wybor == '3':
            print(f"Wynik: {liczba1} * {liczba2} = {pomnoz(liczba1, liczba2)}")

        elif wybor == '4':
            wynik = podziel(liczba1, liczba2)
            print(f"Wynik: {liczba1} // {liczba2} = {wynik}")
    else:
        print("Nieprawidłowy wybór, spróbuj ponownie.")

kalkulator()
