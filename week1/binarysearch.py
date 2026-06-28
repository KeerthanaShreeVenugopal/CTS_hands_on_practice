import random


def binary_search(array, target) -> int:

    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            return mid

        if array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


nums = [ 13, 16, 35, 43, 54, 92]
target = 13
idx = binary_search(nums, target)
print(idx)  # O/P: 1