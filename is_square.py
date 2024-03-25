def is_square(n):
    if n < 0:  
        return False
    sqrt_n = n ** 0.5  
    return sqrt_n.is_integer()  