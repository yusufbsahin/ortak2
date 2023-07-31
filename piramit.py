while True:
    try:
        n = int(input("Bir sayı girin: "))
        if n <= 0 or n % 2 == 0:
            raise ValueError("Lütfen pozitif ve tek bir sayı girin.")
        break
    except ValueError as ve:
        print("Hatalı giriş! " + str(ve))

print("\n".join((i * "*").center(n * 2) for i in range(1, n * 2, 2)))
