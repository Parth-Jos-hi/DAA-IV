'''Question:- Given a sorted array of non-negative integers, design an efficient algorithm to search for a given key element
              using the Jump Search technique. Implement the algorithm using a program and determine whether the key element
              is present in the array or not.
              Also, compute the total number of comparisons required for each input case.'''

import math

def jump_search(arr, key):
    n = len(arr)
    comparisons = 0

    step = int(math.sqrt(n))
    prev = 0

    # Jumping phase
    while prev < n and arr[min(step, n) - 1] < key:
        comparisons += 1
        prev = step
        step += int(math.sqrt(n))

        if prev >= n:
            return False, comparisons

    # Linear search phase
    while prev < min(step, n):
        comparisons += 1
        if arr[prev] == key:
            return True, comparisons
        prev += 1

    return False, comparisons


test_cases = int(input("Enter number of test cases: "))

while test_cases > 0:
    n = int(input("Enter the size of the array: "))
    print("Enter the sorted array elements (space separated):")
    arr = list(map(int, input().split()))
    key = int(input("Enter the key element to search: "))

    is_present, comparisons = jump_search(arr, key)

    if is_present:
        print("Present", comparisons)
    else:
        print("Not Present", comparisons)

    test_cases -= 1
