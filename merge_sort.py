from sort_utility import is_list_sorted


def merge_sort(in_list):
    """ Returns sorted list.

    Keyword arguments:
    in_list -- input list to be sorted
    """
    out_len = len(in_list)

    # Base cases for the recursion
    # List sizes of 1 and 2
    if out_len <= 1:
        return in_list
    elif out_len == 2:
        if in_list[0] > in_list[1]:
            return [in_list[1], in_list[0]]
        else:
            return in_list

    # Divide the input list into two sides
    left_len = out_len // 2
    right_len = out_len - left_len
    left_side = in_list[:left_len]
    right_side = in_list[left_len:]

    # Generate the output list
    out_list = in_list

    # Recursive call the sort on the left- and right-hand sides of the
    # input list.
    left_side = merge_sort(left_side)
    right_side = merge_sort(right_side)

    # Merge the now sorted left- and right-hand sides
    left_index = 0
    right_index = 0

    for out_index in range(out_len):
        if (left_index < left_len) and (right_index < right_len):
            if (left_side[left_index] <= right_side[right_index]):
                out_list[out_index] = left_side[left_index]
                left_index += 1
            else:
                out_list[out_index] = right_side[right_index]
                right_index += 1
        elif (left_index < left_len):
            out_list[out_index] = left_side[left_index]
            left_index += 1
        else:
            out_list[out_index] = right_side[right_index]
            right_index += 1
    return out_list

print merge_sort(["a", "a", "c", "a"])
print is_list_sorted([True, False, True])
print merge_sort(["abc", "aab", "caa", "-**"])
print merge_sort([True, True, False, True, False])
print merge_sort([1])
print "one"
print merge_sort([2, 1])
print "two"
print merge_sort([1, 2])
print "two"
print merge_sort([1, 2, 3])
print "three"
print merge_sort([1, 1, 1])
print "three"
print merge_sort([1, 1, 2])
print "three"
print merge_sort([1, 3, 5, 7, 9])
print "five"
print merge_sort([1, 3, 5, 7, 9, 2, 4, 6, 8])
print "done"
print merge_sort([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
print merge_sort([9, 9, 9, 9, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 1])
