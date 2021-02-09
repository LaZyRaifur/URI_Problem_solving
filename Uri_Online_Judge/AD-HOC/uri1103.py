while True:
    try:
        a,b,x,y = list(map(int,input().split()))
        if a==0 and b==0 and x==0 and y==0:
            break
        else:
            res =  ((x*60)+y)-((a*60)+b)
            if res <0:
                print(res + 1440)
            else:
                print(res)

    except EOFError:
        break