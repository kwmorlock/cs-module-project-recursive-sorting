# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    #puts back together here
    #sorting happe ns here

    # Your code here
    a = 0
    b = 0
    k = 0

    for k in range(0, elements):
        #comparing a to b
        #if a is bigger put it in array and iterate both
        #if b is bigger put it in array and iterate both
        #if a is out of range, push b and iterate
        #if b is out of range, push a and iterate


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here

