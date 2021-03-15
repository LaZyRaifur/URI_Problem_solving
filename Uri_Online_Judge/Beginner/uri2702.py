def value_stock():
    a,b,c = map(int,input().split())
    return a,b,c
def vale_demand():
    x,y,z = map(int,input().split())
    return x,y,z
def result(a,b,c,x,y,z):
    sum = 0
    if a<x:
        sum += x-a
    if b<y:
        sum += y - b
    if c<z:
        sum += z - c
    return sum

a,b,c = value_stock()
m,n,o = vale_demand()
print(result(a,b,c,m,n,o))
