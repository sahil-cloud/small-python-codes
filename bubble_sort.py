def bubble(a):
    for j in range(0,len(a)-1):
        for i in range(0,len(a)-1-j):
            if(a[i]>a[i+1]):
                a[i],a[i+1]=a[i+1],a[i]

a=[2,13,41,12,32,11,255,1]
bubble(a)
print(a)