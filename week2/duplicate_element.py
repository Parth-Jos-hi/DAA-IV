def left_element(arr, target):
    st = 0
    ed = len(arr) - 1
    key = -1
    while st <= ed:
        mid = st + (ed - st) // 2
        if arr[mid] == target:
            key = mid
            ed = mid - 1
        elif arr[mid] < target:
            st = mid + 1
        else:
            ed = mid - 1

    return key


def right_element(arr, target):
    st = 0
    ed = len(arr) - 1
    key = -1
    while st <= ed:
        mid = st + (ed - st) // 2
        if arr[mid] == target:
            key = mid
            st = mid + 1
        elif arr[mid] < target:
            st = mid + 1
        else:
            ed = mid - 1

    return key


arr = [1,2,2,2,2,2,2,2,2,3,4,5]
target = 2
left = left_element(arr, target)
right = right_element(arr, target)
duplicates = right - left + 1

print(f"duplicate elements : {duplicates}")
