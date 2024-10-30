from utils import is_prime


def main(limit: int = 10_001) -> int:
    result = 1

    index = 0
    while index < limit:
        result += 1
        if is_prime(result):
            index += 1

    return result

if __name__ == "__main__":
    result = main()
    print(result)