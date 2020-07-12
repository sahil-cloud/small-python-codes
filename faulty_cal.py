#calculator
num=input("type of operator want to use")
m = float(input("enter number"))
n=float(input("enter 2nd number"))

if m==45 and n==2 and num=="*":
    print("4000")
if m==56 and n==6 and num=="/":
    print("6")
if m==400 and n==3 and num=="-":
    print("3")
if num=="+":
    print(m+n)
elif num=="-":
    print(m-n)
elif num=="*":
    print(m*n)
else :
    print(m/n)
