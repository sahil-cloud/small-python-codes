def pyr(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end="")
        print()        

n=6
pyr(n)

#rotate 180
def pyra(n):
    k=2*n-2
    for i in range(0,n):
       for j in range(0,k):
           print(end=" ")
        k=k-2   
        for j in range(0,i+1):
            print("*",end="")
        print()           

n=6
pyra(n)
