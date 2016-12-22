import math

def legendre(a, p):
    if a % p == 0:
        leg = 0
        return leg
    else:
        nums = []
        x = []
        for i in range(p):
            nums.append(i)
        for num in nums:
            if a % p == num**2 % p:
                x.append(num)
        if len(x) > 0:
            return(1, x)
        else:
            return -1
def euler_legendre(a, p):
    exp = 4
    leg = (a**exp) % p
    if leg > p//2:
        return int(leg-p)
    else:
        return int(leg)

def gauss_legendre(a, p):
    residues = []
    neg_residues = []
    for i in range(2, 9):
        if (i*a) % p <= p//2:
            residues.append((i*a) % p)
        else:
            residues.append(((i*a) % p) - p)
            neg_residues.append(((i*a) % p) - p)
    return residues, len(neg_residues)

def eisenstein(a, p):
    a_vals = []
    for i in range(1, int(p//2)+1):
        a_vals.append(int(math.floor(i*a/p)))
    return a_vals, sum(a_vals)

for i in range(1,17):
    print(i,'      ',euler_legendre(i, 17))
                    
        
