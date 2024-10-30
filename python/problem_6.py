def main(limit: int = 100) -> int:
    result = 0

    # param1 = 0
    # param2 = 0

    # for i in range(1, limit + 1):
    #     param1 += i ** 2
    #     param2 += i

    # result = param2 ** 2 - param1
    
    sum = limit * (limit + 1) / 2
    sum_square = ((2 * limit) + 1) * (limit + 1) * limit / 6
    
    result = sum ** 2 - sum_square

    return result

if __name__ == "__main__":
    result = main()
    print(result)