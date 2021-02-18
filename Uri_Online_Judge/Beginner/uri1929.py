def calculation(a,b,c):
    if abs(b-c)<a<(b+c):
        if abs(a-c)<b<(a+c):
            if abs(a-b)<c<(a+b):
                return True
    else:
        False



def mainBody(a,b,c,d):
    if calculation(a,b,c) or calculation(b,c,d) or calculation(a,c,d) or calculation(a,b,d):
        print('S')
    else:
        print('N')
def main():
    a,b,c,d = map(int,input().split())
    mainBody(a,b,c,d)
main()
