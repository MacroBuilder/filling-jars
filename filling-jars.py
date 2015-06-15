def fill(array, num_jars, array_length):
    average = 0
    for index in range(array_length):
        a, b, k = array[index][0], array[index][1], array[index][2]
        average += (b + 1 - a)*k/float(num_jars)
    return int(round(average,1))

N, M = (int(i) for i in raw_input().strip().split())

test_list = []
for _ in range(M):
    test_list.append([int(i) for i in raw_input().strip().split()])

print fill(test_list,N,M)
