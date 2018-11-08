def solution(A): # maxEndSum defines the maximum sum ending at a particular element.
    n = len(A)
    maxEndSum = A[0]
    maxSliceSum = A[0]
    for i in range(1, n):
        maxEndSum = max(0, maxEndSum + A[i])
        maxSliceSum = max(maxSliceSum, maxEndSum)

    return maxSliceSum


ans = solution([5, -7, 3, 5, -2, 4, -1])
print(ans)