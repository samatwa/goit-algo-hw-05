def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0

    while low <= high:
        mid = (low + high) // 2
        iterations += 1

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return (iterations, arr[mid])

    # Якщо елемент не знайдено, то повертаємо верхню межу
    if high < 0:
        return (iterations, arr[0])
    if low >= len(arr):
        return (iterations, None)
    return (iterations, arr[low])


# Example usage:
arr = [0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5, 1.7, 1.9]
x = 1.6
result = binary_search(arr, x)
print(result)
