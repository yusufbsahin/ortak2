n = int(input("Bir sayı girin: "))

print("\n".join((i*"*").center(n*2) for i in range(1, n*2, 2)))
