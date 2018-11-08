def gcd(a,b):
    if a%b == 0:
        return b;
    else:
        return gcd(b, a%b)


def removeCommonPrimeDivisors(x, y):
    """ If x has only y's prime divisors, it returns 1"""
    while x!=1:
        g = gcd(x, y)
        if g == 1:
            break
        x /= g

    return x


def haveCommonPrimeDivisors(x, y):
    g = gcd(x, y)
    """ GCD has all the common prime divisors for two numbers
        We will remove common prime divisors from gcd and both numbers to see both have any divisors other than of gcd's """

    if removeCommonPrimeDivisors(x, g) == 1 and removeCommonPrimeDivisors(y, g) == 1:
        return True
    else:
        return False


def solution(A, B):
    count = 0
    for x, y in zip(A,B):
        if haveCommonPrimeDivisors(x, y):
        #if removeCommonPrimeDivisors(x, y) == 1 and removeCommonPrimeDivisors(y, x) == 1:  # this eliminates the use of haveCommonDivisors()
            count+=1

    return count


ans = solution([10, 16, 15, 1], [20, 24, 75, 1])
print(ans)