if __name__ == '__main__': #creatinng main syntax
    arr = [] #declearing empty array
    n = int(input("Enter the length of the array"))
    for i in range(n-1):
        m = int(input("Enter the element/number"))
        arr.append(m)


        def findmissing(arr, n):
            expected_sum = n * (n + 1) / 2
            actual_sum = sum(arr)
            return expected_sum - actual_sum


    missing_number = findmissing(arr,n)
    print("the missing number is {}".format(missing_number))