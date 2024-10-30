from utils import is_palindrome


# need optimization
def main(digit_number: int = 3) -> int:
    result = int()
    
    lower, upper = 10 ** (digit_number - 1), (10 ** digit_number) - 1
    
    for i in range(lower, upper):
        for j in range(lower, upper):
            product = i * j
            if (is_palindrome(product)):
                if product> result:
                    result = product
    


    return result

if __name__ == "__main__":
    result = main()
    print(result)
    

    # result = int()
    # lower, upper = 10 ** (digit_number - 1), (10 ** digit_number) - 1
    # prev = 1000000000000
    # a = upper
    # while a >= lower:
    #     if a % 11 == 0:
    #         b = upper
    #         db = 1
    #     else:
    #         b = 990
    #         db = 11
        
    #     while b >= a:
    #         if a*b <= result:
    #             pass
    #         condition = prev > a * b
    #         if not condition:
    #             print(condition)
    #         prev = a * b
    #         if is_palindrome(a * b):
    #             result = a *b 
    #         b -= db
    #     a -= 1