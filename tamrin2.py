def sieve_of_eratosthenes(n):

    """Implements the Sieve of Eratosthenes algorithm."""

    prime = [True for i in range(n + 1)]

    p = 2

    while (p * p <= n):

        if (prime[p] == True):

            for i in range(p * p, n + 1, p):

                prime[i] = False

        p += 1

    return prime



def   calculate_amount(n, m):

    """Calculates the amount based on the given conditions."""

    prime = sieve_of_eratosthenes(n)

    count = 0

    for i in range(2, n + 1):

            if not prime[i]:

                count += 1

            if count == m:

                if prime[m]:

                    return -1

                else:

                    return m * 10**9

    return -1





n = int(input())

m = int(input())





amount = calculate_amount(n, m)

print(amount)
