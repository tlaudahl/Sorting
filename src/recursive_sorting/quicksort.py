# Decide on base case

# Find the pivot point

# Partition our data to the left and right of our pivot
# left -> smaller than pivot, right -> larger than pivot
# What if they're the same size as the pivot? Just pick one? >=

# repeat, recurse


my_list = [5, 9, 3, 7, 2, 8, 1, 6]

def partition(data):
    left = []
    pivot = data[0]
    right = []

    for item in data[1:]:
        if item < pivot:
            left.append(item)
        else: # Handling > or =
            right.append(item)

    return left, pivot, right


def quicksort(data):
    if data == []:
        return data
    left, pivot, right = partition(data)

    return quicksort(left) + [pivot] + quicksort(right)


print(quicksort(my_list))