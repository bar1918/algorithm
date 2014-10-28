import random


def quick_sort(in_list):
    """ Returns sorted list.

    Keyword arguments:
    in_list -- input list to be sorted

    Uses a couple of helper routines to perform the work and is
    required in this implementation to allow in-place memory usage.

    The trivial pre-processing step performed in this routine takes
    the input list and passes it along with pointers to first and last
    element to the recursive routine _quick_sort().

    The additional _quick_sort_swap() and _quick_sort_pivot are helper
    functions for _quick_sort()
    """

    _quick_sort(in_list, 0, (len(in_list) - 1))


def _quick_sort_swap(in_list, index_x, index_y):
    """ Swaps in_list[index_x] with in_list[index_y]"""

    temp = in_list[index_y]
    in_list[index_y] = in_list[index_x]
    in_list[index_x] = temp


def _quick_sort(in_list, start_index, stop_index):
    """Returns the sorted sublist--in_list[start_index : stop_index + 1].

    Keyword arguments:
    in_list -- input list to be sorted
    start_index -- pointer to first element of the sub list
    stop_index -- pointer to last element of the sub list

    This implementation first partions the input sub list around a randomly
    chosen pivot point.
    Then recursively calls itself on the two sub-partitions
    The base case for the recursion is a sublist of size one.
    """

    # Base cases for the recursion
    # Sub-list less than two elements
    if (start_index > (stop_index - 1)):
        return

    # Choose a pivot point
    # Move pivot element to the beginning of sublist and start the partition.
    # The partition requires that all list items to the left of the pivot
    # should be less than the pivot and vice versa when partition process
    # is complete.
    # The last step is to swap the in_list[start_index] into the
    # correct pivot position.
    pivot_point = start_index + random.randrange(stop_index - start_index + 1)
    _quick_sort_swap(in_list, pivot_point, start_index)

    # Partions input sublist around the pivot
    partition_index = start_index
    for unpartition_index in range((start_index + 1), stop_index + 1):
        if in_list[unpartition_index] < in_list[start_index]:
            # increment partition pointers
            partition_index += 1
            # Only perform the swap when larger items have been found in the
            # partitioning of the sublist.
            if (partition_index != unpartition_index):
                _quick_sort_swap(in_list, partition_index, unpartition_index)

    # Move the pivot value to the correct position in the sub list
    _quick_sort_swap(in_list, start_index, partition_index)

    # Recursively calls _quick_sort on the two partitions
    _quick_sort(in_list, start_index, partition_index)
    _quick_sort(in_list, partition_index + 1, stop_index)
