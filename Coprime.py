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
    
def totient(n):
    return len(list_coprimes(n))

totients = []
products =[]
for i in range(2, 60):
    product = 1
    totients.append(totient(i))
    coprimes = list_coprimes(i)
    for j in range(len(coprimes)):
        product = product*coprimes[j]
    if product% i == i-1:
        print(i,' ', -1)
    else:
        print(i, ' ', product%i)
    

        
