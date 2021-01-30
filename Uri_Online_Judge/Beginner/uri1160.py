a = int(input())

for i in range(1,a+1):
    pa,pb,g1,g2 = input().split()
    sum = 0
    while(pa<pb):
        sum = sum + 1
        pa = int(pa)+(int(pa)*(round(float(g1))/100))
        pb = int (pb) + (int(pb)*(round(float(g2))/100))

    if sum<100:
        print("%d anos."%(sum+1))
    else:
        print("Mais de 1 seculo.")