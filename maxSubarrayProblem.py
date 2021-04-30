import csv
import time
from resource import getrusage, RUSAGE_SELF, getpagesize
data = []
csvdata = open('data.csv')
reader = csv.reader(csvdata, delimiter=';')

for row in reader:
    data.append([int(x) for x in row])

arr_no = 4

#######################################################################################################################

# Kadanes Algorithm
def kadane(arr):
    # var x will be used to store the maximum sum sublist found so far
    # var y will be used to store the maximum sum of sublist ending at current position
    x, y = 0, 0 

    for i in arr:
        # updating the maximum sum of sublist ending for index i in the array
        y = y + i 
        # if the maximum sum is negative, set it to zero
        y = max(y, 0)
        # updating the result if the current sublist sum is found to be greater than the previous stored one
        x = max(x, y)
    # return the best possible outcome for the maximum sum of a given array
    return x

#######################################################################################################################

# Testing Kadanes Algorithm
print("--------------------------------")
print("Kadane's Algorithm")
print("--------------------------------")

for i in range(0, 5):
    start = time.time()
    print(kadane(data[arr_no]))
# mem_bytes = int(getrusage(RUSAGE_SELF).ru_maxrss)
# mem_mb = "{:.2f}".format(mem_bytes * 0.000001)
    end = time.time()
    time_ms = (end - start) * 1000
    print("Elapsed runtime:", f'{time_ms:.8f}', "ms")
print("")

#######################################################################################################################

# Divide and Conquer Algorithm
def maxCrossSub(arr, l, m, h):
 
    # elements left of mid
    max_cross_sum = 0
    left_sum = 0
 
    for i in range(m, l-1, -1):
        max_cross_sum = max_cross_sum + arr[i]
 
        if (max_cross_sum > left_sum):
            left_sum = max_cross_sum

    # elements right of mid
    max_cross_sum = 0
    right_sum = 0

    for j in range(m + 1, h + 1):
        max_cross_sum = max_cross_sum + arr[j]
 
        if (max_cross_sum > right_sum):
            right_sum = max_cross_sum
 
    # return sum of element left and right of mid
    return max(left_sum + right_sum, left_sum, right_sum)
 

def maxSubArray(arr, l, h):
 
    # base case for one
    if (l == h):
        return arr[l]
 
    # finding the middle point m
    m = (l + h) // 2
 
    # return maximum of three possible cases
    return max(maxSubArray(arr, l, m),
               maxSubArray(arr, m+1, h),
               maxCrossSub(arr, l, m, h))
 
#######################################################################################################################

# Testing Divide and Conquer Algorithm
print("--------------------------------")
print("Divide-and-Conquer Algorithm")
print("--------------------------------")

for i in range (0, 5):
    start = time.time()
    print(maxSubArray(data[arr_no], 0, len(data[arr_no])-1))
    end = time.time()
    time_ms = (end - start) * 1000
    print("Elapsed runtime:", f'{time_ms:.8f}', "ms")

print("")