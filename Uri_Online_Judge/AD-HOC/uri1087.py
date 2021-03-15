def valu_input():
    a, b, m, n = map(int, input().split())
    return (a,b,m,n)
while True:
    a,b,m,n = valu_input()
    if (a+b+m+n) == 0:
        break
    if (a==m) and (b==n):
        print(0)
        continue
    if (a==m) or (b==n):
        print(1)
        continue
    if (abs(a-m))==(abs(b-n)):
        print(1)
        continue
    print(2)


