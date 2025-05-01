def isPrime(n):
    for num in range(2, n):
        if n % num == 0:
            return False
    return True

def minOperations(n):
    # Initialization 
    factors = []
    
    # Iteration
    while n != 1:
        for num in range(2, n + 1):
            if n % num == 0 and isPrime(num):
                factors.append(num)
                n //= num
                break
    return sum(factors)

