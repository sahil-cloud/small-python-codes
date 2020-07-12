"""guess=18
num=5#number of guesses
while(num!=0):
    m=int(input("enter the number"))
    num=num-1
    if m>18:
        if num==0:
            print("game over")
        else:
            print("enter lesser number")
        #num=num-1
    elif m<18:
        if num==0:
            print("game over")
        else:
            print("enter greater number")
        #num=num-1
    else:
        if num==0:
            print("game over")
        else:    
            print("you won",end=" ")
            print("no of attempts",5-num)
        break
    #num=num-1
"""

