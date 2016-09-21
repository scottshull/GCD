a = 270
b = 192

def gcd(a, b):
    while (a != 0) and (b != 0):
        r = a % b
        a = b
        b = r
    return a

print (gcd(a, b))
