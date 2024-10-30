def main(limit: int = 1000, divisors: list[int] = [3, 5]) -> int:
    result = 0
    for number in range(1, limit):
        for divisor in divisors:
            if number % divisor == 0:
                result += number
                break
    return result

if __name__ == "__main__":
    result = main()
    print(result)