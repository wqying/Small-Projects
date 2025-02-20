def is_prime(num):
    if num > 1:  # no negative prime numbers
        for i in range(2, (num // 2) + 1):  # n/2 because anything bigger than that means the other multiplier is 1
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


print(is_prime(75))
