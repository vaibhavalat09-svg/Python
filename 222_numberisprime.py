def check_prime(num):
    if num <= 1:
        print(num, "is not a Prime number")
    else:
        for i in range(2, num):
            if num % i == 0:
                print(num, "is not a Prime number")
                break
        else:
            print(num, "is a Prime number")

check_prime(7)
check_prime(10)