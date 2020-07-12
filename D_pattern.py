line=13
for i in range(0,line):
    for j in range(0,line):
        if(i==0 or i==line-1):
            if(j==line-1):
                print(" ",end=" ")
            else:
                print("*",end=" ")
        for k in range(1,line-1):
            if(i==k):
                if(j==0 or j==line-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
    print("")                