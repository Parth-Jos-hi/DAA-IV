''' Question:- Count Duplicate Elements in an Array'''



def count_duplicates(arr):
    freq = {}
    duplicates = 0

    # Count frequency of each element
    for x in arr:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1

    # Count total duplicate occurrences
    for x in freq:
        if freq[x] > 1:
            duplicates += freq[x] - 1

    return duplicates



t = int(input("Enter number of test cases: "))

for test in range(1, t + 1):
    print(f"\nTest Case {test}")

    n = int(input("Enter number of elements: "))
    arr = []

    print("Enter the elements one by one:")
    for _ in range(n):
        arr.append(int(input()))

    result = count_duplicates(arr)

    print("Number of duplicate elements:", result)
