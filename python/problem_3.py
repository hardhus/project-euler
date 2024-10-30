def main(number: int = 600851475143) -> int:
    result = 1
    
    while number % 2 == 0:
        result = 2
        number //= 2

    for potenial_factor in range(3, int(number**.5) + 1, 2):
        while number % potenial_factor == 0:
            result = potenial_factor
            number //= potenial_factor

    if number > 1:
        result = number


    return result

if __name__ == "__main__":
    result = main()
    print(result)