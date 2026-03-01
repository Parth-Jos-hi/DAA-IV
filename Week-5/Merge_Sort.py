''' Question:-  Implement Merge Sort in Python to sort an array of integers using the Divide and Conquer approach.'''


# Merge function to combine two sorted subarrays
def merge(arr, left, mid, right):
    # Create left and right subarrays
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    i = 0  # Pointer for L
    j = 0  # Pointer for R
    k = left  # Pointer for main array

    # Compare elements and merge in sorted order
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy remaining elements of L (if any)
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy remaining elements of R (if any)
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


# Recursive Merge Sort function
def merge_sort(arr, left, right):
    # Divide array until single element remains
    if left < right:
        mid = (left + right) // 2  # Find middle index

        merge_sort(arr, left, mid)      # Sort left half
        merge_sort(arr, mid + 1, right) # Sort right half

        merge(arr, left, mid, right)    # Merge sorted halves




if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter elements separated by space: ").split()))

    print("Original Array:", arr)

    merge_sort(arr, 0, n - 1)

    print("Sorted Array:", arr)
