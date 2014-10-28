def count_inversions(in_list):
    """ Returns number of inversions in the list and returns the sorted list.

    Keyword arguments:
    in_list -- input list to be sorted
    """
    out_len = len(in_list)

    # Base cases for the recursion
    # List sizes of 1 and 2
    if out_len == 0:
        return 0, in_list
    elif out_len == 1:
        return 0, in_list
    elif out_len == 2:
        if in_list[0] > in_list[1]:
            return 1, [in_list[1], in_list[0]]
        else:
            return 0, in_list

    # Divide the input list into two sides
    left_len = out_len // 2
    right_len = out_len - left_len
    left_side = in_list[:left_len]
    right_side = in_list[left_len:]

    # Generate the output list
    out_list = in_list

    # Recursive call the sort on the left- and right-hand sides of the
    # input list.
    inversions_left, left_side = count_inversions(left_side)
    inversions_right,  right_side = count_inversions(right_side)

    # Merge the now sorted left- and right-hand sides
    left_index = 0
    right_index = 0

    # Start with the sum of the number of inversions found on the right- and
    # left-side of the list. Add to these the "split inversions" found when
    # merging right- and left-sides of list.
    number_inversions = inversions_left + inversions_right

    for out_index in range(out_len):
        if (left_index < left_len) and (right_index < right_len):
            if (left_side[left_index] <= right_side[right_index]):
                out_list[out_index] = left_side[left_index]
                left_index += 1
            else:
                out_list[out_index] = right_side[right_index]
                number_inversions += left_len - left_index
                right_index += 1
        elif (left_index < left_len):
            out_list[out_index] = left_side[left_index]
            left_index += 1
        else:
            out_list[out_index] = right_side[right_index]
            right_index += 1
    return number_inversions, out_list
