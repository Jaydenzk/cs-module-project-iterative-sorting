# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # TO-DO: swap
        # Your code here
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    k = 0
    for _ in range(0, len(arr) - (1)):
        swapped = False
        # Loop through your array
        for i in range(0, len(arr) - (1 + k)):
            # Compare each element to its neighbor
            # If elements in wrong position (relative to each other, swap them)
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i + 1], arr[i]
                swapped = True
        k = k + 1
        # If no swaps performed, stop.
        if swapped == False:
            break


    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here
    if len(arr) == 0:
        return []

    # set up k + 1 buckets, where k is max value in arr
    maximum = max(arr)
    count = [0 for _ in range(maximum + 1)]

    # increment the count for each index for every corresponding value in arr
    for item in arr:
        if item < 0:
            return "Error, negative numbers not allowed in Count Sort"

        count[item] = count[item] + 1

    # modify the count arr to have a running total of items
    for i in range(1, len(count)):
        count[i] = count[i] + count[i - 1]

    # for each item in arr, use the count arr value at that index to place item,
    # then decrement the value in count arr by 1
    arr_sorted = [None for _ in range(len(arr))]
    for item in arr:
        arr_sorted[count[item] - 1] = item
        count[item] = count[item] - 1


    return arr
