def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Time: O(N)
    Space: O(1)"""
    for i in range(len(items) - 1):

        if items[i] > items[i+1]:
            return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Time: O(N^2)
    Space: O(1)"""

    for i in range(len(items)):

        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j+1], items[j]

    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    for i in range(len(items)):

        low_index = i
        for j in range(i, len(items)):

            if items[j] < items[low_index]:
                low_index = j

        items[i], items[low_index] = items[low_index], items[i]

    return items


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    for j in range(1, len(items)):

        old_index = j
        while j >= 0:

            if items[j-1] > items[old_index] and j >= 1:
                j -= 1
            else:
                items.insert(j, items.pop(old_index))
                break


items = [50, 41, 18, 26, 49, 26, 32, 49, 49,
         31, 10, 41, 22, 26, 24, 5, 35, 39, 4, 11]
insertion_sort(items)
print(items)
