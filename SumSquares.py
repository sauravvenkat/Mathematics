def factors(n):
    factors = []
    for i in range(1, n//2+1):
        if n%i==0:
            factors.append(i)
    factors.append(n)
    return factors

def sum_squares(n):

    nums1 = []
    for i in range(0, n+1):
        nums1.append(i)
    num_list1 =[]
    for num in nums1:
        for num2 in reversed(nums1):
            if num**2 + num2**2 == n and num <= num2:
                num_list1.append([num, num2])
    return(num_list1)

print(sum_squares(15625),len(sum_squares(15625)) )

n = int(input("Enter a value: "))

for i in range(n+1):
    squares = sum_squares(i)
    if squares == []:
        print(i,' none')
    else:
        print(i,' ', squares, len(squares))
