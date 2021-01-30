first = 0
while True:
       try:


            a = int(input())
            b = 0
            order = 1
            if first:
                print('')
            first = 1
            if(a%4==0) and (not(a%100==0) or (a%400==0)):
                print("This is leap year.")
                b = 1
                order = 0
            if(a%15==0):
                print("This is huluculu festival year.")
                order = 0
            if(a%55==0) and b:
                print("This is bulukulu festival year.")

            # if(a%4 !=0 or a%100!=0 or a%400 != 0 or a%15!=0 or a%55!=0):
            #     print("This is an ordinary year.")
            if order:
                print("This is an ordinary year.")


       except EOFError:
           break
