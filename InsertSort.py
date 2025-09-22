def insert_sort(A):
    length=len(A)
    for i in range(1,length):
        for j in range(i,0,-1):
            if A[j]<A[j-1]:
                A[j],A[j-1]=A[j-1],A[j]
            else:
                break
    return A
