def findPeaks(A):
    n = len(A)
    peaks = []
    for i in range(1, n - 1):
        if A[i] > A[i + 1] and A[i] > A[i - 1]:
            peaks.append(i)

    return peaks


def findFactors(n):
    factors = []
    i = 2
    while (i * i <= n):
        if n % i == 0:
            factors.append(i)
        i = i + 1

    for i in range(len(factors) - 1, -1, -1):
        if factors[i] * factors[i] != n:
            factors.append(int(n / factors[i]))

    return factors


def solution(A):
    n = len(A)
    peaks = findPeaks(A)
    n_peaks = len(peaks)
    factors = findFactors(n)
    #print(peaks, factors)

    for f in range(len(factors) - 1, -1, -1):
        if factors[f] <= n_peaks:
            lenP = n / factors[f]
            #print("lenP", lenP)
            count = 0
            for i in range(0, len(peaks)):
                if (peaks[i]) // lenP == count:
                    count += 1
                    #print(count)

            if count == factors[f]:
                return factors[f]

    if n_peaks > 0:
        return 1

    return 0


ans = solution([2, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 1, 3, 1])
print(ans)