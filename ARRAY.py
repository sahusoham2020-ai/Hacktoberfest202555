# Python3 implementation to increment 
# values in the given range by a value d 
# for multiple queries

# structure to store the (start, end) 
# index pair for each query

# function to increment values in the given range
# by a value d for multiple queries
def incrementByD(arr, q_arr, n, m, d):

    sum = [0 for i in range(n)]

    # for each (start, end) index pair perform 
    # the following operations on 'sum[]'
    for i in range(m):

        # increment the value at index 'start' 
        # by the given value 'd' in 'sum[]'
        sum[q_arr[i][0]] += d

        # if the index '(end+1)' exists then decrement
        # the value at index '(end+1)' by the given
        # value 'd' in 'sum[]'
        if ((q_arr[i][1] + 1) < n):
            sum[q_arr[i][1] + 1] -= d

    # Now, perform the following operations:
    # accumulate values in the 'sum[]' array and
    # then add them to the corresponding indexes
    # in 'arr[]'
    arr[0] += sum[0]
    for i in range(1, n):
        sum[i] += sum[i - 1]
        arr[i] += sum[i]

# function to print the elements 
# of the given array
def printArray(arr, n):

    for i in arr:
        print(i, end = " ")
        
# Driver Code
arr = [ 3, 5, 4, 8, 6, 1]

q_arr = [[0, 3], [4, 5], [1, 4],
         [0, 1], [2, 5]]

n = len(arr)
m = len(q_arr)

d = 2

print("Original Array:")
printArray(arr, n)

# modifying the array for multiple queries
incrementByD(arr, q_arr, n, m, d)

print("\nModified Array:")
printArray(arr, n)

# This code is contributed
# by Mohit Kumar
