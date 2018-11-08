"""def solution(A): #General solution using sorting O(n log n)
    B = list(A)
    A.sort()
    n = len(A)
    count = 0
    half = n//2
    print("half ", half)
    for i in range(n):
        if A[i] == A[half]:
            count += 1

    if count > half:
        return B.index(A[half])
    else:
        return -1
"""


def solution(A):  # based on stack. Adds each element, removes 2 elements when top 2 are different. O(N)
    n = len(A)
    value = -1
    size = 0
    #index = -1
    for x in range(n):
        if size == 0:
            size+=1
            value = A[x]
            #index = x
            #print(value, " ", index,"\n")
        else:
            if value != A[x]:
                size-=1
            else:
                size+=1

    if size == 0:
        return -1

    count = 0
    for i in range(n):  # Value is not always leader, it is only candidate, need to check if it is leader or not.
        if A[i] == value:
            count += 1

    if count > n//2:
        return A.index(value)
    else:
        return -1


ans = solution([1,2,2,2,2,1,1,1])
print(ans)
