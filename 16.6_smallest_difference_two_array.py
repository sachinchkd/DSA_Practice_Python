array1 = [23, 5, 10, 17, 30]
array2 = [26, 134, 135, 14, 19]


def smallest_difference(array1,array2):
    min_diff = float('inf')
    smallest_pair = (None, None)

    for i in range(len(array1)):
        for j in range(len(array2)):
            diff = abs(array1[i]-array2[j])

            if diff < min_diff:
                min_diff = diff
                smallest_pair = (array1[i],array2[j])
    return min_diff, smallest_pair

print(smallest_difference(array1, array2))