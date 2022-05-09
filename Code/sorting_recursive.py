#!python
import random


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: o(n) all cases, it must traverse the entirity of both arrays to combine them
    TODO: Memory usage: o(n) all cases, it builds an array containing all elements of both arrays"""

    if not items1 and not items2:
        return []
    elif not items1:
      # Recurse in items2 until empty
        return [items2[0]] + merge(items1, items2[1:])
    elif not items2:
      # Recurse in items1 until empty
        return [items1[0]] + merge(items1[1:], items2)
    else:
        if items1[0] < items2[0]:
            return [items1[0]] + merge(items1[1:], items2)
        else:
            return [items2[0]] + merge(items1, items2[1:])


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: o(nlogn) in all cases, since the items input is halved n times
    TODO: Memory usage: o(n) in all cases, since it is not done in place and must create a new array"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order
    if len(items) == 1:
        return items
    else:
        midpoint = len(items) // 2
        left = merge_sort(items[:midpoint])
        right = merge_sort(items[midpoint:])
        items2 = merge(left, right)

    for i in range(len(items2)):
        items[i] = items2[i]

    return items


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: pivot on farthest right array element) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: o(n) in all cases, must iterate through the entire array to move elements into the correct spot
    TODO: Memory usage: o(1) in all cases, items is modified in-place"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p

    pivot_index = high

    pointer_index = low
    for i in range(low, high):
        if items[i] <= items[pivot_index]:
            items[i], items[pointer_index] = items[pointer_index], items[i]
            pointer_index += 1

    items[pointer_index], items[pivot_index] = items[pivot_index], items[pointer_index]

    return pointer_index


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: o(nlogn) if pivots are always directly in the middle of each partition
    TODO: Worst case running time: o(n^2) if elements in each partition are already sorted and pivot is rightmost
    TODO: Memory usage: o(n) in worst case, o(logn) in average case. Worst case occurs when items are sorted, increasing
    the callstack to n size. In the average case, fewer recursive calls are required and the callstack is smaller."""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort

    if low == None:
        low = 0

    if high == None:
        high = len(items) - 1

    if low < high:
        pivot = partition(items, low, high)

        quick_sort(items, low, pivot - 1)
        quick_sort(items, pivot + 1, high)


def partition_subarrays(items):
    pivot = items[0]

    left, right = [], []

    for i in range(1, len(items)):

        if items[i] <= pivot:
            left.append(items[i])
        else:
            right.append(items[i])

    return left, right, pivot


def quick_sort_subarrays(items):
    if len(items) <= 1:
        return items
    else:
        left, right, pivot = partition_subarrays(items)
        return quick_sort_subarrays(left) + [pivot] + quick_sort_subarrays(right)


items = [24, 31, 23, 35, 15, 39, 5, 19, 39,
         20, 15, 25, 40, 29, 12, 39, 24, 34, 36, 41]
print(quick_sort_subarrays(items))
