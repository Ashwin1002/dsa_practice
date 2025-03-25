def merge_sort(nums):
    if len(nums) < 2:
        return nums
    half = len(nums) // 2
    # print("half => " + str(half))
    sorted_left_side = merge_sort(nums[:half])
    sorted_right_side = merge_sort(nums[half:])
    # print("left => " + str(sorted_left_side))
    # print("right => " + str(sorted_right_side))
    return merge(sorted_left_side, sorted_right_side)
    pass


def merge(first, second):
    final = []
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    while i < len(first):
        final.append(first[i])
        i += 1
    while j < len(second):
        final.append(second[j])
        j += 1
    return final