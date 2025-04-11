def find_primes(a, b):
    primes = []
    for i in range(a, b+1):
        if i  < 2:
            continue
        
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
        
    return primes
            
print(find_primes(10,30))
print(find_primes(1,20))