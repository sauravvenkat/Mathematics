def is_coprime(n,a):
    if a==1:
        return True
    else:
        while a != 1:
            r1 = n%a
            n = a
            a = r1
            if a == 0:
                return False
        return True
def find_ind(n):
    x = 0
    while x >= 0:
        if 3**x % 16 == n :
            return x
        else:
            x += 1

def list_coprimes(n):
    coprimes = [1]
    zero_coprime=[1, -1]
    if n==0:
        return zero_coprime
    elif n==1:
        return "none"
    else:
        for i in range(2,n):
            if is_coprime(n, i) == True:
                coprimes.append(i)
        return coprimes

def findD():
    n = 1
    while n >= 1:
        if n**n % 17 == 2:
            return n
        else:
            n += 1
def findC():
    x = 1
    while x>=1:
        if 2**x == 7**(x**2) % 17:
            return x
        else:
            x += 1
def findA():
    n = 1
    while n >= 1:
        if 5**n % 17 == 12:
            return n
        else:
            n +=1

def totient(n):
    return len(list_coprimes(n))

def factors(n):
    factors = []
    for i in range(1, n//2+1):
        if n%i==0:
            factors.append(i)
    factors.append(n)
    return factors

def order(n, m, factors):
    for factor in factors:
        if(n**factor) % m == 1:
            return(factor)
for i in range(1, 17):
    print(i,' ', find_ind(i))
a = int(input('Enter a: '))
m = int(input('Enter m: '))
for i in range(0, a+1):
    if i == 0:
        print(i,' has an order of', 0, 'in mod 17')
    else:
        print(i,' has an order of',order(i, m, factors(totient(m))),'in mod 17')

