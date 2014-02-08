import math
while(1):
    n = int(input("Enter p-2, p is a prime"))
    p = math.factorial(n)
    ans = p % (n+2)
    print(ans)
