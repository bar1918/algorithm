The depot contains a number of implementations of algortihms in python.

These have been tested for accuracy, but not for performance.

The following algorithms have been implemented:
    1) count_inversions_py
        Counts the number of inversions in a list
    2) merge_sort.py
        Sorts a list using the merge sort algoithm
    3) quick_sort.py
        Sorts a list using the quick sort algorithm. 
        Merge sort will usually run faster than quick sort, but the quick
        sort algorithm performs the sort in place, i.e., it doesn't require
        a sperate copy of the list.
    4) sort_utility.py
        Contains utility functions to help with testing.
        a) is_list_sorted(): Returns True if the list is sorted.
    5) order_statistics.py
	    Computes the order statistics on a list.
		The 0th order statistic is the minimum value in the list.
		The 1st order statistic is the second smallest element in the list.
		The nth order statistic is the maximum value in the list.
		(Where n is the len of the list.)
		see: http://en.wikipedia.org/wiki/Order_statistic
		The median is  the middle element in a sorted list.
