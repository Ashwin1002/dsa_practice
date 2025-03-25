def median_of_three(arr, low, high):
    mid = (low + high) // 2
    a, b, c = arr[low], arr[mid], arr[high]
    
    # Find the median value and swap it with arr[high] to use as the pivot
    if (a <= b <= c) or (c <= b <= a):
        arr[mid], arr[high] = arr[high], arr[mid]
    elif (b <= a <= c) or (c <= a <= b):
        arr[low], arr[high] = arr[high], arr[low]
    
    return arr[high]  # The pivot is now at arr[high]

def partition(arr, low, high):
    pivot = median_of_three(arr, low, high)
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot correctly
    return i + 1  # Return partition index

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  # Partitioning index
        quick_sort(arr, low, pi - 1)  # Sort left subarray
        quick_sort(arr, pi + 1, high)  # Sort right subarray

# Example usage:
arr = [24, 9, 29, 14, 19, 27]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
