"""
O(M*N)


impact = {'A': 1, 'C': 2, 'G': 3, 'T': 4}


def findLeast(i, j, S):
    minImpact = impact[S[i]]
    for a in range(i, j+1, 1):
        if impact[S[a]] < minImpact:
            minImpact = impact[S[a]]
    return minImpact


def solution(S, P, Q):
    sol =[]
    #i = 0
    for a, b in zip(P, Q):
        sol.append(findLeast(a, b, S))
    return sol


ans = solution("CAGCCTA", [2, 5, 0], [4, 5, 6])
print(ans)"""


def solution(S, P, Q):
    genomePrefix =  [[0 for x in range(len(S) + 1)] for y in range(3)]  # No need for T
    for i, char in enumerate(S):
        a = g = c = 0
        if char == 'A':
            a = 1
        elif char == 'C':
            c =1
        elif char == 'G':
            g = 1
        # prefix arrays for each neucleotide. 1 if present, 0 for absent
        genomePrefix[0][i + 1] = genomePrefix[0][i] + a
        genomePrefix[1][i + 1] = genomePrefix[1][i] + c
        genomePrefix[2][i + 1] = genomePrefix[2][i] + g

    sol = []
    for i, val in enumerate(P):
        start = P[i]
        end = Q[i]+1  # Prefix array starts with 0 and has length 1 more than len of string
        if genomePrefix[0][end] - genomePrefix[0][start] > 0:
            sol.append(1)
        elif genomePrefix[1][end] - genomePrefix[1][start] > 0:
            sol.append(2)
        elif genomePrefix[2][end] - genomePrefix[2][start] > 0:
            sol.append(3)
        else:
            sol.append(4)

    return sol


ans = solution("CAGCCTA", [2, 5, 0], [4, 5, 6])
print(ans)