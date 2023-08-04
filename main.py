def bubble_sort(arr: list):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# Example usage; this won't execute unless you run `main.py`
if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(bubble_sort(numbers))
