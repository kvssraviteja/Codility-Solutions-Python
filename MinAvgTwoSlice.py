def prefix_sums(A):
    n = len(A)
    P = [0]*(n+1)
    P[0] = 0
    for i in range(1, n+1):
        P[i] = P[i-1] + A[i-1]

    return P


def count(P, i, j):
    return P[j+1] - P[i]


def solution(A, n):
    minAvg = float("inf")
    minIndex = 0
    P = prefix_sums(A)
    for i in range(0, n-2):
        if minAvg > count(P, i, i+1)/2.0:
            minAvg = count(P, i, i+1)/2.0
            minIndex = i

        if minAvg > count(P, i, i + 2) / 3.0:
            minAvg = count(P, i, i + 2) / 3.0
            minIndex = i

    if minAvg > count(P, n-2, n-1) / 2.0:
        minAvg = count(P, n-2, n-1) / 2.0
        minIndex = n-2

    print(minAvg)
    return minIndex


ans = solution([4, 2, 2, 5, 1, 5, 8], 7)
print(ans)
P = prefix_sums([4, 2, 2, 5, 1, 5, 8])
print(P, count(P, 1 , 2))