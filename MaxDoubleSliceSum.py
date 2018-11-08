"""
#O(n**2) Solution


def maxSum(A): # maxEndSum defines the maximum sum ending at a particular element.
    n = len(A)
    maxEndSum = 0
    #maxSliceSum = 0
    for i in range(1, n):
        maxEndSum = max(0, maxEndSum + A[i])
        #maxSliceSum = max(maxSliceSum, maxEndSum)

    return maxEndSum


def solution(A):  # finding maximum sum from both directions ending at an element. Then adding the arrays to find the maximum
    n = len(A)
    B = list(A)
    B.reverse()
    maxS = []
    maxRev = []
    for i in range(1, n-1):
        maxS.append(maxSum(A[:i]))
        maxRev.append(maxSum(B[:(n-1-i)]))

    sumMax = [x + y for x, y in zip(maxS, maxRev)]
    return max(sumMax)
    #print(max, maxRev) """


def solution(A):  # Calculate end sum upto i and begin sum from i + 2, and find max. O(N) solution
    n = len(A)
    maxEndIndex = [0]*n
    maxBeginIndex = [0]*n
    maxEndSum = 0
    maxBeginSum = 0
    for i in range(1, n - 2):
        maxEndSum = max(0, A[i] + maxEndSum)
        maxEndIndex[i] = maxEndSum

    for i in range(n-2, 1, -1):
        maxBeginSum = max(0, A[i] + maxBeginSum)
        maxBeginIndex[i] = maxBeginSum

    sumMax = 0
    for i in range(0, n-2):
        sumMax = max(sumMax, maxEndIndex[i] + maxBeginIndex[i+2])

    return sumMax
    # print(max, maxRev) """


ans = solution([3, 2, 6, -1, 4, 5, -1, 2])
print(ans)

ans = solution([5, 17, -1, 3])
print(ans)

