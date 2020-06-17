# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    middle = (start + end) // 2 
    if len(arr) == 0: #if length is zero we return an index of neg 1
        return -1
    if arr [middle] == target: #if the middle index matches target then we return that middle value
        return middle
    elif arr [middle] > target: #if target is less than middle its checking left side
        return binary_search(arr, target, end, middle - 1) #if its on left side it will always be less than middle which is why its -1 to middle, middle is decreasing
    else:
        return binary_search(arr, target, start, middle + 1) #if target is more than the middle than checking on the right side, which is why +1
#add from start, and subtract from end

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here