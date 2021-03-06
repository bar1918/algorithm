import random


def order_statistics(in_list, kth):
    """ Returns nkth order statistic for a list.

    Keyword arguments:
    in_list -- input list from which we compute the order statistic
    kth -- is the kth order statistic that we need to find in the list

    The 0th order statistic is the minimum value in the list.
    The 1st order statistic is the second smallest element in the list.
    The nth order statistic is the maximum value in the list.
    (Where n is the len of the list.)
    see: http://en.wikipedia.org/wiki/Order_statistic
    The median is  the middle element in a sorted list.
    Uses a couple of helper routines to perform the work and is
    required in this implementation to allow in-place memory usage.

    The trivial pre-processing step performed in this routine takes
    the input list and passes it along with pointers to first and last
    element to the recursive routine _order_statistic().

    The additional _order_statistic_swap() and _order_statistic_pivot
    are helper functions for _order_statistic()
    """

    if (kth >= len(in_list)):
        kth = len(in_list) - 1

    # Check for empty lists and negative order statistics
    if (kth < 0):
        return
    else:
        return _order_statistics(in_list, 0, (len(in_list) - 1), kth)


def _order_statistics_swap(in_list, index_x, index_y):
    """ Swaps in_list[index_x] with in_list[index_y]"""

    temp = in_list[index_y]
    in_list[index_y] = in_list[index_x]
    in_list[index_x] = temp


def _order_statistics(in_list, start_index, stop_index, kth):
    """Returns the order statistic from -- in_list[start_index : stop_index + 1].

    Keyword arguments:
    in_list -- input list to be sorted
    start_index -- pointer to first element of the sub list
    stop_index -- pointer to last element of the sub list
    kth -- is the kth order statistic that we need to find in the list
    This implementation first partions the input sub list around a randomly
    chosen pivot point.
    Then recursively calls itself on the two sub-partitions
    The base case for the recursion is a sublist of size one.
    """

    # Base cases for the recursion
    # Sub-list less than two elements indicates that you find the
    # order statistic kth
    if (start_index >= (stop_index - 1)):
        return in_list[start_index]

    # Choose a pivot point
    # Move pivot element to the beginning of sublist and start the partition.
    # The partition requires that all list items to the left of the pivot
    # should be less than the pivot and vice versa when partition process
    # is complete.
    # The last step is to swap the in_list[start_index] into the
    # correct pivot position.
    pivot_point = start_index + random.randrange(stop_index - start_index + 1)
    _order_statistics_swap(in_list, pivot_point, start_index)

    # Partions input sublist around the pivot
    partition_index = start_index
    for unpartition_index in range((start_index + 1), stop_index + 1):
        if in_list[unpartition_index] < in_list[start_index]:
            # increment partition pointers
            partition_index += 1
            # Only perform the swap when larger items have been found in the
            # partitioning of the sublist.
            if (partition_index != unpartition_index):
                _order_statistics_swap(in_list, partition_index,
                                       unpartition_index)

    # Move the pivot value to the correct position in the sub list
    _order_statistics_swap(in_list, start_index, partition_index)

    # Check on which side of the partition the kth order statistic
    # lies and recursively call _order_statistic on that partition.
    if (partition_index == kth):
        return in_list[partition_index]
    elif (partition_index < kth):
        return _order_statistics(in_list, partition_index + 1, stop_index, kth)
    else:
        return _order_statistics(in_list, start_index, partition_index, kth)
