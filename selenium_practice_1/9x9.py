def bublesort(a):
    l = len(a)
    print(a)
    for i in range(1,l):
        for j in range(1,l):
            if a[j-1] > a[j]:
                r =a[j-1]
                a[j-1]=a[j]
                a[j]=r
    print(a)
def nineXnine():
    for i in range(1,10):
        for j in range(1,i+1):
            print('%d * %d =%d'%(j,i,i*j),end= ' ')
        print()
