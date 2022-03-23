A=[33,23,87,84,49,12,32,68,71,39,88]
for i in range(0,11,1):
    a=divmod(A[10-i],13)
    A[i]=a[1]+10
    print(i,A[i])
print()
for i in range(1,11,1):
    b=divmod(A[11-i],11)
    A[i-1]=b[1]
    print(i,A[11-i])
print()
print(A)