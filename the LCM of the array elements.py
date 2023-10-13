import math
def LCMofArray(a):
    lcm =a[0]
    for i in range(1,len(a)):
        lcm = lcm*a[i]//math.gcd(lcm,a[i])
        return lcm
arr1 =[1,2,3]
arr2 =[2,3,4]
arr3=[4,5,6]
print("LCM of arr1 elements:", LCMofArray(arr1))
print("LCM of arr2 elements:", LCMofArray(arr2))
print("LCM of arr3 elements:", LCMofArray(arr3))