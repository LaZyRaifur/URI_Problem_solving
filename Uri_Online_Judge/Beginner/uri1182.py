n = int(input())
s= input()

m =[]
for i in range(12):
    m.append([])
for i in range(12):
    for j in range(12):
        x = float(input())
        m[i].append(x)

if s == 'S':
    sum = 0
    for k in range(12):
        sum += m[k][n]
    print(sum)
if s == 'M':
    mid = 0
    sum = 0
    for k in range(12):
        sum += m[k][n]
    mid = sum/12
    print('{:.1f}'.format(mid))