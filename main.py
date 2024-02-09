def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

while True:
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Wyjście")

    wybór = input("Wpisz numer operacji (1/2/3): ")

    if wybór in ('1', '2'):
        num1 = float(input("Wpisz pierwszą liczbę: "))
        num2 = float(input("Wpisz drugą liczbę: "))

        if wybór == '1':
            print("Wynik dodawania:", dodawanie(num1, num2))
        elif wybór == '2':
            print("Wynik odejmowania:", odejmowanie(num1, num2))
    
    elif wybór == '3':
        print("Do widzenia!")
        break
    else:
        print("Nieprawidłowy wybór!")
