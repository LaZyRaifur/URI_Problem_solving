def obtained_number(list):
    a,b = int(list[0]),int(list[2])
    c= list[1]
    if a == b:
        return a*b
    if c.isupper():
        return b-a
    else:
        return a+b

t = int(input())
for i in range (t):
    m = input()
    print(obtained_number(m))
