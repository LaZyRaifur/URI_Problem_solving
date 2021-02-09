a = []
for i in range(0,4):
    x= int(input())
    a.append(x)
j = 1
for j in range(i,4):
    if a[i]>a[j]:
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
for i in range(0,4):
    print(a[i])