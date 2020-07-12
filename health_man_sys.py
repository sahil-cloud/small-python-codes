#3 names AVI SAHIL ROHAN 
#1 diet and 2 exercise
# datetime 
from datetime import datetime
a=str(datetime.now())
print(a)
   
b=int(input("1. for DIET  2. for EXERCISE"))
c=input("A for AVI, S for SAHIL , R for ROHAN ")
if b==1:
    d=input("input diet")
else:
    e=input("input exercise")

if c=="A":
    if b==1:
        f=open("avi1.txt","a")
        f.write(d)
        f.write("  ")
        f.write(a)
    else :
        f=open("avi2.txt","a")
        f.write(e)
        f.write("  ")
        f.write(a)
    f.close()    
if c == "S":
    if b == 1:
        f = open("sahil1.txt", "a")
        f.write(d)
        f.write("  ")
        f.write(a)
    else:
        f = open("sahil2.txt", "a")
        f.write(e)
        f.write("  ")
        f.write(a)
    f.close()
if c == "R":
    if b == 1:
        f = open("rohan1.txt", "a")
        f.write(d)
        f.write("  ")
        f.write(a)
    else:
        f = open("rohan2.txt", "a")
        f.write(e)
        f.write("  ")
        f.write(a)
    f.close()    
