#import numpy as np

def arrayF(N):
    num_array = [0] * (N+1)
    i = 2
    while i * i <= N:
        if num_array[i] == 0:
            k = i*i #we need to start from i*i as i*1, i*2,.. i*(i-1) are already covered by previous i's. i=5, 2*5 is covered when i =2
            while k<=N:
                if num_array[k] == 0:
                    num_array[k] = i
                k = k+i
        i = i+1
    return num_array


def Solution(N, P, Q):
    m = len(P)
    bool_arrayF = [True]*(N+1)
    count_arrayF = [0]*(N+1)
    num_arrayF = arrayF(N)
    count = 0
    for i in range(4, N+1):
        if num_arrayF[i] > 0:
            if num_arrayF[int(i/num_arrayF[i])] == 0:
                bool_arrayF[i] = False
                count += 1
        count_arrayF[i] = count
    result = []
    for i in range(m):
        result_num = count_arrayF[Q[i]] - count_arrayF[P[i]-1]
        result.append(result_num)

    return result


print(Solution(26, [1,4,16], [26,10,20]))