a= int(input())
while a>0:
    a -= 1
    name,value = input().split()
    if (name == 'Thor'):
        print("Y")
    else:
        print("N")