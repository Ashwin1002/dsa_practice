# Given a set of distinct integers, return all possible subsets.
# Time complexity: O(2^n)
# Space complexity: O(n2^n)
def power_set(input_set):
    if not input_set:
        return set()
    final = [[]]
    for n in list(input_set):
        new = []
        for m in final:
            new.append(m + [n])
        final.extend(new)
        
    return final
    pass
