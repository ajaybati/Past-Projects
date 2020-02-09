i=input("What number do you want for the pyramid: ")
q=int(i)
h=int(i)+1
for x in range(1,h,1):
    for z in range(1,q,1):
        print(" ", end =' ')
    for u in range(1,x+1,1):
        print("*"+"   ", end='')
    print()
    q-=1
    
    





    
