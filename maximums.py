# Replace the "ANSWER HERE" for your answer

def max_of_two(x, y):

    if x>=y:
        return x
    else:
        return y

def max_of_three(x, y, z):

    if x>=y and x>=z:
        return x
    elif x<y and z<y:
        return y
    else:
        return z

print(max_of_two(5,4)) # Retorna: 5

print(max_of_two(-2,-3)) # Retorna: -2

print(max_of_two(0,0)) # Retorna: 0

print(max_of_three(5,4,7)) # Retorna: 7

print(max_of_three(-2,-3,-1)) # Retorna: -1

print(max_of_three(0,0,0)) # Retorna: 0
