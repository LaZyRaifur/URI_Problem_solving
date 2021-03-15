a = int(input())
while a>0:
    a -= 1
    i = input()
    res = bin(int(i)).count('1')
    print(res)