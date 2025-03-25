def bubble_sort(nums):
    """
    Sorts a list of numbers using the bubble sort algorithm.

    Args:
        nums (list): A list of numbers to be sorted.

    Returns:
        list: A new list containing the sorted numbers.

    The function works by repeatedly stepping through the list,
    comparing adjacent elements and swapping them if they are in the
    wrong order. This process is repeated until the list is sorted.

    The space complexity of the algorithm is `O(n)` while time complexity is `O(n^2)` on worst case and 'O(n)` on best case.
    """
    swapping = True
    end = len(nums)
    sorted_list = nums.copy()
    while swapping:
        swapping = False
        for i in range(1, end):
            first = sorted_list[i - 1]
            second = sorted_list[i]
            print(f"first {first} second {second}")
            if first > second:
                sorted_list[i -1] = second
                sorted_list[i] = first
                swapping = True
        end -= 1
        print(f"list => {sorted_list}  and last index {end}")
    return sorted_list
    pass
