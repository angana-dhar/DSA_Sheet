def sum_1(arr):
    result = 0
    for x in arr:
        result += x
    return result
if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    print ('sum_1: {}'.format(sum_1(arr)))

def sum_2(arr):
    result = sum(arr)
    return result


if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    print ('sum_2: {}'.format(sum_2(arr)))
