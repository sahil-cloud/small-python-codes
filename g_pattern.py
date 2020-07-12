line=7
row=5
for i in range(0,line):
    for j in range(0,row):
        if (i == 0 or i == line-1):
            if(j == 0 or j == row-1):
                print("  ",end=" ")
            else:
                print("*",end=" ")       
        if  (i==1 or i==2):
            if(j==0):
                print("*",end=" ")
            else:
                print("  ",end=" ")
        if(i==line-2 or i==line-3):
            if(j==0 or j==row-1):
                print("*",end=" ")
            else:
                print("  ",end=" ")
        if(i==3):
            if(j==1):
                print("  ",end=" ")
            else:
                print("*",end=" ")
    print("")         
            



        

