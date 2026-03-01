''' Question:-  Implement Quick Sort using a randomly selected pivot.
                The program should:
                ->Accept multiple test cases
                ->Sort the given array using Quick Sort
                ->Count the number of comparisons and swaps
                ->Display the sorted array along with comparison and swap count'''


import random
import time


# Partition function using random pivot
def partition(arr, low, high, counters):
    # Select random pivot
    pivot_index = random.randint(low, high)
    pivot = arr[pivot_index]

    i = low
    j = high

    # Rearrange elements around pivot
    while i <= j:

        # Move i forward
        while arr[i] < pivot:
            counters[0] += 1  # Count comparison
            i += 1
        counters[0] += 1

        # Move j backward
        while arr[j] > pivot:
            counters[0] += 1  # Count comparison
            j -= 1
        counters[0] += 1

        # Swap elements if needed
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            counters[1] += 1  # Count swap
            i += 1
            j -= 1

    return i


# Quick Sort function
def quick_sort(arr, low, high, counters):
    if low < high:
        index = partition(arr, low, high, counters)

        quick_sort(arr, low, index - 1, counters)
        quick_sort(arr, index, high, counters)


# ---------------- Main Program ----------------
if __name__ == "__main__":

    random.seed(time.time())

    T = int(input("Enter number of test cases: "))

    while T > 0:
        n = int(input("Enter number of elements: "))

        arr = []
        for _ in range(n):
            arr.append(int(input()))

        counters = [0, 0]  # [comparisons, swaps]

        quick_sort(arr, 0, n - 1, counters)

        print("Sorted Array:", *arr)
        print("Comparisons:", counters[0])
        print("Swaps:", counters[1])

        T -= 1
