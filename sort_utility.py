def is_list_sorted(in_list):
    """ Returns True if list is sorted."""
    in_list_len = len(in_list)
    if in_list_len <= 1:
        return True
    else:
        for list_index in range(in_list_len-1):
            if (in_list[list_index] > in_list[list_index + 1]):
                return False
        return True

