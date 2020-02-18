# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = []
    # TO-DO
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] > arrB[0]:
            merged_arr.append(arrB[0])
            arrB.pop(0)
        elif arrA[0] < arrB[0]:
            merged_arr.append(arrA[0])
            arrA.pop(0)
    if len(arrA) == 0:
        merged_arr.extend(arrB)
    elif len(arrB) == 0:
        merged_arr.extend(arrA)
    return merged_arr


# print(merge([18, 24, 11, 16, 14], [6, 4, 7, 2, 8, 1]))
# print(merge([11, 14, 16, 18, 24], [8, 10, 13, 20, 21, 23]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    else:
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]
        print(f'left: {left}, right: {right}')
        left = merge_sort(left)
        right = merge_sort(right)
    arr = merge(left, right)
    print(f'merged: {arr}')
    return arr

merge_sort([5,18,2,8,25,1,9,3,11,19])
merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
