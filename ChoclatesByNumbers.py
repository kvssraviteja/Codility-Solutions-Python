def gcd(a,b):
    if a%b == 0:
        return b;
    else:
        return gcd(b, a%b)


def solution(N, M):
    g = gcd(N,M)
    return int(N/g)


ans = solution(1, 4)
print(ans)
