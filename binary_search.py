def binary_search_with_upper_bound(arr, value):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = left + (right - left) // 2

        if arr[mid] == value:
            # Find the upper bound for the value (smallest element greater than or equal to value)
            upper_bound = arr[mid]
            break
        elif arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    # If upper_bound is not found in the loop, then value is not present, and we set upper_bound to the left pointer
    if upper_bound is None:
        if left < len(arr):
            upper_bound = arr[left]
        else:
            # If left is outside of array bounds, it means value is greater than all elements in arr
            upper_bound = None

    return iterations, upper_bound

arr = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]
target = 4.5

print(binary_search_with_upper_bound(arr, target))