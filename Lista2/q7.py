def prime_list():
    def is_prime(num):
        for i in range(2,int(num**0.5)+1):
            if num % i == 0 and num != 2:
                return False
        return True
    
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1