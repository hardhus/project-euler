def main(limit: int = 4_000_000) -> int:
    result = 0
    previous, current = 0, 1
    while current < limit:
        previous, current = current, previous + current
        if current % 2 == 0:
            result += current
    return result

if __name__ == "__main__":
    result = main()
    print(result)