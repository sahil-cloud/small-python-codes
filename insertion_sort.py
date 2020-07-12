a=[1,2,21,12,0,23,19,4,5]
for i in range(0,len(a)):
    key=a[i]
    j=i-1
    while j>=0 and key<a[j]:
        a[j+1]=a[j]
        j -= 1
    a[j+1]=key
print("sorted arry using insertion sort is",a)