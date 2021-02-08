def fib(n):
    a,b = 0,1
    while b<n:
        yield  a
        a,b = b,a+b
table = list(fib(10000))
while True:
    try:
        n,m = map(int,input().split())

    except EOFError:
        break
    print(table[(table[n])]%m)