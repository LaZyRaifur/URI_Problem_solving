import math
def prime(x):
    res = 1
    for i in range(2,int(math.sqrt(x))+1):
        if (x%i==0):
            res = 0
            print("Not Prime")
            break
        else:
            continue
    if res == 1:
       print("Prime")
       return res

a = int(input())
# for i in (1,a+1):
while a>0:
    a -= 1
    n = int(input())
    ans = prime(n)
