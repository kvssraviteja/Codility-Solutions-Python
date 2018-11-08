def solution(A):
    n = len(A)
    maxValue = max(A)
    count = {}
    for element in A:
        if element in count:
            count[element] +=1
        else:
            count[element] = 1

    divisors = {}

    for element in A:
        divisors[element] = [1]

    divisor = 2
    # while divisor <= maxValue:
    #     if divisor in A:
    while divisor*divisor <= maxValue:
        element_candidate = divisor
        while element_candidate <= maxValue:
            if element_candidate in divisors and not divisor in divisors[element_candidate]:
                divisors[element_candidate].append(divisor)
                #if element_candidate/divisor in A:
                #   divisors[element_candidate].append(element_candidate/divisor)
            element_candidate += divisor
        divisor +=1

    for element in divisors:
        temp = [int(element / div) for div in divisors[element]]
        # Filter out the duplicate divisors
        temp = [item for item in temp if item not in divisors[element]]
        divisors[element].extend(temp)


    final_count = [0]*n
    for i, element in enumerate(A):
        final_count[i] = len(A) - sum(count.get(divisor, 0) for divisor in divisors[element])

    return final_count


print(solution([3,1,2,3,6]))
