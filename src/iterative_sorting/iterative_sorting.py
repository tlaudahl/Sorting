# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Start the for loop one index ahead of the above for loop since the above for loop is already "sorted"
        for j in range(i + 1, len(arr)):
            # If element at smallest index is greater than element at index j
            if arr[smallest_index] > arr[j]:
                # Set smallest index to new index of smallest element
                smallest_index = j
        # Assign arr[i] to temp so we dont lose the value
        temp = arr[i]
        # set arr[i] to the new smallest element
        arr[i] = arr[smallest_index]
        # set old smallest element to the old value at arr[i].. swapping them
        arr[smallest_index] = temp
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # Need a swapped variable since we need to run a pass everytime we swap a value, even once.
    swapped = True
    while swapped:
        # Set swapped to false so the loop stops running if element at index i is never greater than the element at index i + 1
        swapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                # store a temp variable equal to element at index i, so we can assign the next element in the array equal to it
                temp = arr[i]
                # Set element at index i to be the value of the next element
                arr[i] = arr[i+1]
                # Set the next element in the array equal to the old value of the element at the current index, which is why we stored it in a temp variable
                arr[i+1] = temp
                # Set swapped back to true so the loop runs again, since we DID swap values at least once
                swapped = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr