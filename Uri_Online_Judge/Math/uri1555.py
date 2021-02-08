a = int(input())
while a>0:
    raf = 0
    bet = 0
    car = 0
    a -= 1
    x,y = input().split()
    x = int(x)
    y = int(y)
    raf = ((3*x)*(3*x))+(y*y)
    bet = 2*(x*x) + ((5*y)*(5*y))
    car = -(100*x) + (y*y*y)
    if((raf>bet)and(car>bet)):
        if (raf>car):
            print("Rafael ganhou")
        else:
            print("Carlos ganhou")
    elif((raf<bet)and(raf<car)):
        if(bet>car):
            print("Beto ganhou")
        else:
            print("Carlos ganhou")
    elif((raf>car)and(bet>car)):
        if(raf>bet):
            print("Rafael ganhou")
        else:
            print("Beto ganhou")