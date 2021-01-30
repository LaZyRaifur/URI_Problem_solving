par = []
impar = []
res = 0
for i in range(15):
    value = int(input())
    if (value %2 == 0):
        par.append(value)
    else:
        impar.append(value)
    if (len(par)==5):
        element = 0
        for i in par:
            print("par[%d] = %d"%(element,i))
            element += 1
        par = []
    if (len(impar) == 5):
        element = 0
        for j in impar:
            print("impar[%d] = %d"%(element,j))
            element += 1
        impar = []

if(len(impar)>0):
         element = 0
         for k in impar:
                print("impar[%d] = %d"%(element,k))
                element +=1
         impar = []
if (len(par)>0):
            element = 0
            for l in par:
                print("par[%d] = %d"%(element,l))
                element+=1
            par = []

