def hitta_primtal(n):
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  

    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

    primtal = [p for p in range(2, n + 1) if is_prime[p]]
    return primtal

n = int(input("Ange ett heltal mellan 1 och 99: "))
if 1 <= n <= 99:
    primtal_lista = hitta_primtal(n)
    print(f"Primtal mellan 2 och {n}: {primtal_lista}")
else:
    print("Felaktig inmatning. Ange ett heltal mellan 1 och 99.")
