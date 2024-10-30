from utils import is_prime


# need optimization
def main(limit: int = 2_000_000) -> int:
    result = 0

    for i in range(limit):
        if is_prime(i):
            result += i

    return result

if __name__ == "__main__":
    result = main()
    print(result)