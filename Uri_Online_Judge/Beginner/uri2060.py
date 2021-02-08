a = int(input())
arr = input().split()
two = 0
th = 0
fo = 0
fi = 0
for i in range(a):


    if int(arr[i])%2==0:
        two+= 1
    if int(arr[i])%3==0:
        th += 1
    if int(arr[i])%4==0:
        fo += 1
    if int(arr[i])%5==0:
        fi += 1

print("%d Multiplo(s) de 2"%two)
print("%d Multiplo(s) de 3"%th)
print("%d Multiplo(s) de 4"%fo)
print("%d Multiplo(s) de 5"%fi)
