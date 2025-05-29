fact_cache = {0: 1, 1: 1}

def factorial(n):
    if n in fact_cache:
        return fact_cache[n]
    
    result = factorial(n - 1) * n
    fact_cache[n] = result
    return result

print("factorial for 6 = ", factorial(6)) 
print("factorial for 3 = ", factorial(3))  
print("factorial for 8 = ", factorial(8))  
