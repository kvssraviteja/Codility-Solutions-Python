def solution1(A):  # based on stack. Adds each element, removes 2 elements when top 2 are different. O(N)
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
        return -1, -1

    count = 0
    for i in range(n):  # Value is not always leader, it is only candidate, need to check if it is leader or not.
        if A[i] == value:
            count += 1

    if count > n//2:
        #print("count: ", count)
        return A.index(value), count
    else:
        return -1, -1


def solution(A): # Only leader can be equileader, check for leader in left part and right part each time
    n = len(A)
    leader, count = solution1(A)
    if (count == -1):
        return 0
    lcount = 0
    equiCount = 0
    for i in range(n-1):
        if A[i] == A[leader]:
            lcount += 1
        rcount = count - lcount
        if lcount > (i+1)//2 and rcount > (n-i-1)//2 :
            equiCount += 1

    return equiCount

ans = solution([1,2,2,2,2,1,1,2])
print(ans)