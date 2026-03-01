''' Question:-  Implement Insertion Sort and counts the number of comparisons and shifts performed during sorting.'''


def insertion_sort_count(arr):
    comparisons = 0
    shifts = 0
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if arr[j] > key:
                arr[j + 1] = arr[j]
                shifts += 1
                j -= 1
            else:
                break

        arr[j + 1] = key

    return comparisons, shifts



t = int(input("Enter number of test cases: "))

for test in range(1, t + 1):
    print(f"\nTest Case {test}")

    n = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter the elements: ").split()))

    comparisons, shifts = insertion_sort_count(arr)

    print("Sorted Array:", *arr)
    print("Number of Comparisons:", comparisons)
    print("Number of Shifts:", shifts)
