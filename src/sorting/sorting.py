# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    maxA = len(arrA)
    maxB = len(arrB)
    elements = maxA + maxB
    merged_arr = [0] * elements

    # Your code here
    iA = 0
    iB = 0
    for i in range(elements):
        if iA == maxA:
            merged_arr[i] = arrB[iB]
            iB += 1
            continue
        elif iB == maxB:
            merged_arr[i] = arrA[iA]
            iA += 1
            continue
        if arrA[iA] < arrB[iB]:
            merged_arr[i] = arrA[iA]
            iA += 1
        else:
            merged_arr[i] = arrB[iB]
            iB += 1
        
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # Base case
    if len(arr) == 1 or arr == []:
        return arr
    else:
        mid = (len(arr)) // 2
        A = merge_sort(arr[mid:])
        B = merge_sort(arr[:mid])
        arr = merge(A,B)

        return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
