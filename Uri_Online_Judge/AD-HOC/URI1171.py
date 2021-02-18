a = int(input())
list = {}
for i in range(a):
    x = int(input())
    if(x in list):
        list[x] += 1
    else:
        list[x] = 1

count =  list.keys()
count = sorted(count)
for k in count:
    print("%d aparece %d vez(es)"%(k,list[k]))
