def factorielle(n: int) -> int:
    if n < 0:
        raise ValueError("n doit être positif")

    if n <= 1:
        return 1

    return n * factorielle(n - 1)


def est_premier(n: int) -> bool:
    if n < 0:
        raise ValueError("n doit être positif")

    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def pgcd(a: int, b: int) -> int:
    if a < 0 or b < 0:
        raise ValueError("Les nombres doivent être positifs")

    while b != 0:
        a, b = b, a % b

    return a