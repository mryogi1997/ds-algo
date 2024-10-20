def validMountainArray(arr):
    n = len(arr)
    if n < 3:  # Must have at least 3 elements
        return False

    i = 0

    # Walk up: Strictly increasing
    while i < n - 1 and arr[i] < arr[i + 1]:
        i += 1

    # Peak cannot be the first or the last element
    if i == 0 or i == n - 1:
        return False

    # Walk down: Strictly decreasing
    while i < n - 1 and arr[i] > arr[i + 1]:
        i += 1

    # If we reached the end, it's a valid mountain array
    return i == n - 1

# Example usages
print(validMountainArray([1, 3, 5, 4, 2]))  # Output: True
print(validMountainArray([0, 2, 3, 4, 5, 2, 1, 0]))  # Output: True
print(validMountainArray([1, 2, 3, 4, 5]))  # Output: False
print(validMountainArray([5, 4, 3, 2, 1]))  # Output: False
print(validMountainArray([2, 1, 2]))  # Output: False
