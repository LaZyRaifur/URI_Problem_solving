a = int(input())
while a>0:
    a -= 1
    pa,pb,g1,g2 = input().split()
    pa = int(pa)
    pb = int(pb)
    g1 = float(g1)
    g2 = float(g2)
    sum = 0
    while pa<=pb:
        pa = int(pa+(pa*g1)/100)
        pb = int(pb+(pb*g2)/100)
        sum += 1
        if sum>100:
            break
    if sum<=100:
        print("%d anos."%(sum))
    else:
        print("Mais de 1 seculo.")