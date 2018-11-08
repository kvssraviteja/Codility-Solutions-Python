def prefix_sums(A):
    n = len(A)
    P = [0]*(n+1)
    P[0] = 0
    for i in range(0, n):
        P[i] = P[i-1] + A[i]

    return P


def count(P, i, j):
    return P[j] - P[i-1]


def mushroom_picker(A, k, m):  # Picker can move in one direction and optionally some steps in opp direction
    n = len(A)
    ans = 0
    P = prefix_sums(A)
    for p in range(min(k, m) + 1):  # loop for initial direction left and then opp
        left = k - p
        right = min(n-1, max(k, k + m - 2 * p))
        ans = max(ans , count(P, left, right))

    for p in range(min(m + 1, n - k)):  # loop for initial direction right and then opp
        right = k + p
        left = max(0, min(k, k - m - 2 * p))
        ans = max(ans , count(P, left, right))

    return ans


ans = mushroom_picker([2,3,7,5,1,3,9], 4, 6)
print(ans)
