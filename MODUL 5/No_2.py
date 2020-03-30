def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai

A = [1,2,3,4,7,9,11,13,23,90]
B = [2,4,9,10,11,12,14,15,19]
C = []
C.extend(A)
C.extend(B)
print ('Nilai C' , C)
