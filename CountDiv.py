import math

"""O(1)"""
"""Another solution : ans = B/K - (A-1)/K plus 1 if A == 0"""


def solution(A, B, K):
    temp = 0
    for i in range(A, B+1):
        if A % K == 0:
            temp = 1  # for cases where A and B are same and divisible by K
            break
        else:
            A = A + 1

    if temp == 0:
        return
    else:
        return 1 + math.floor((B - A)/K)


ans = solution(0, 10, 5)
print(ans)
