def bubble_sort(arr: list: list) -> list:
    """
    Performs a bubble sort in Python
    """

    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# Example usage; this will only execute if you run `main.py`
if __name__ == "__main__":
    import random

    n = 10 # Number of random numbers (exclusive)
    numbers = [int(random.random() * 100) for x in range(n)]
    print(selection_sort(numbers))
