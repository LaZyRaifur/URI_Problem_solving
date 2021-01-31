# def fib(n):
#     if n == 0:
#         return n
#     elif n == 1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)
#
# a = int(input())
# while a>0:
#     a -= 1
#     num = int(input())
#     res = fib(num)
#     print("fib(%d) = %d"%(num,res))
fib = [0,1]
a= 0
b = 1
for i in range(60):
    t = a + b
    fib.append(t)
    a = b
    b = t
n = int(input())
for i in range(n):
    num = int(input())
    print("Fib(%d) = %d"%(num,fib[num]))
