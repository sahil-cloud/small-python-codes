a=[23,2,1,12,65,43,11,14,3,56]
#find minimum first
for j in range(0,len(a)):
    min=a[j]
    for i in range(0,len(a)):
        if(a[i]>min):
            min=a[i]
            temp=a[j]
            a[j]=min 
            a[i]=temp

print("sorted array is",a)

