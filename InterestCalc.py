import math

P = int(input("Enter principal amount"))
r = float(input("Enter rate of interest"))
t = int(input("Enter the number of months"))

exponent = r*t
Interest = P*math.exp(exponent)
print("Interest = {0}".format(Interest))
