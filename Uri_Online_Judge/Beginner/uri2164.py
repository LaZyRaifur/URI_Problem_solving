import math
a = int(input())
c = math.pow((1+math.sqrt(5))/2,a)
d = math.pow((1-math.sqrt(5))/2,a)
res = (c-d)/math.sqrt(5)
print("%.1f"%res)

