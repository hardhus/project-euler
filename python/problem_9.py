def main(param1: int = 1000) -> int:
    result = 0

    for a in range(1, param1 // 3):
        for b in range(a + 1, (param1 - a) // 2):
            c = param1 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                result = a * b * c
                break

    return result

if __name__ == "__main__":
    result = main()
    print(result)