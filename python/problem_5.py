from math import floor, log, sqrt
from utils import is_prime


def main(limit: int = 20) -> int:
    result = 1
    primes = list()

    for number in range(2, limit + 1):
        if is_prime(number):
            primes.append(number)

    powers = [0] * len(primes)
    index = 0  

    while index < len(primes): 
        powers[index] = 1
        if primes[index] <= sqrt(limit):
            powers[index] = floor(log(limit) / log(primes[index]))

        result *= primes[index] ** powers[index]
        index += 1

    return result

if __name__ == "__main__":
    result = main()
    print(result)