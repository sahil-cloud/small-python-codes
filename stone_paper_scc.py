list=["stone","paper","scissor"]
import random as r
c=r.choice(list)
com=0
user=0
draw=0
#print(c)
i=0
while(i<5):
    a=input("enter your choice\n")
    print("computers choice",c)
    if a==c:
        print("match drawn")
        i=i+1
        draw=draw+1
        print("chances left",10-i)
    elif (a=="stone" and c=="paper"):
        print("computer won")
        com=com+1
        i=i+1
        print("chaces left",10-i)
    elif a=="paper" and c=="scissor":
        print("computer won")
        com = com+1
        i = i+1
        print("chaces left", 10-i)
    elif a=="scissor" and c=="stone":
        print("computer won")
        com = com+1
        i = i+1
        print("chaces left", 10-i)
    elif a=="stone" and c=="scissor":
        print("user won")
        user = user+1
        i = i+1
        print("chaces left", 10-i)
    elif a=="paper" and c=="stone":
        print("user won")
        user = user+1
        i = i+1
        print("chaces left", 10-i)
    else:
        print("user won")
        user = user+1
        i = i+1
        print("chaces left", 10-i)
print("user won",user)
print("computer won",com)
print("no of draws",draw)