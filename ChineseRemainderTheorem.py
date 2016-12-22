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


def prime_factors(n):
    factors = []
    for i in range(2, n//2 + 1):
        if n % i == 0 and totient(i) == i -1:
            factors.append(i)
        elif totient(n) == n-1:
            return [1, n]
    return factors

def red_mod(a_vals, n_vals):
    for i in range(len(a_vals)):
        a_vals[i] = a_vals[i] % n_vals[i]
    return a_vals
    
def create_dict (a_vals, n_vals):
    values = {}
    for i in range(len(red_mod(a_vals, n_vals))):
       values[ n_vals[i]] = a_vals[i]
    return values

def check_coprime(dictionary):
    coprime = []
    n_vals = list(dictionary.keys())
    for i in range(len(n_vals)):
        n = 1
        while i+n < len(n_vals):
            if (n_vals[i] < n_vals[i+n] )and not ( is_coprime(n_vals[i], n_vals[i+n])):
                 coprime.append(n_vals[i+n])
                 n += 1
            elif (n_vals[i] > n_vals[i+n]) and not ( is_coprime(n_vals[i], n_vals[i+n])):
                 coprime.append(n_vals[i])
                 n += 1
            n += 1
    return(coprime)

print('--------------------------------------------------------------------------------------------')
print('Please enter at least 2 congruences for x of the form x=a(mod n)')
a_vals = []
n_vals = []
mod_ct = 0
YorN = 'N'
while YorN not in ['Y', 'y']:
    a = int(input('Enter value for a where a is greater than 0: '))
    a_vals.append(a)
    n = int(input('Enter value for n where n is greater than 1: '))
    n_vals.append(n)
    mod_ct = len(create_dict (a_vals, n_vals))
    if mod_ct >= 2:
        YorN = input('Enter Y to stop or N for more mods: ')
        if YorN not in ['Y','y','N','n']:
            while YorN  not in ['Y','y','N','n']:
                 YorN = input('Please input Y or N only: ')
print('--------------------------------------------------------------------------------------------')

print('Your Congruences are: ')
M_vals = []
M = 1
for keys, values in create_dict(a_vals, n_vals).items():
    print('x =', values,'( mod ',keys,')')
    M *= keys
for keys in create_dict(a_vals, n_vals).keys():
    M_vals.append(int(M/keys))

if len(check_coprime(create_dict(a_vals, n_vals))) == len(create_dict(a_vals, n_vals)) - 1:
    print('REMAINDER CANNOT BE FOUND NO VALUES ARE COPRIME')
