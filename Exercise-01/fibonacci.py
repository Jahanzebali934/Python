def fibonacci(n):

    result = []
    a = 1 
    b = 1
    c = 0
    
    while a <= n :
        result.append(a)
        c = a+b
        a = b
        b = c

    return result

print(fibonacci(10))

