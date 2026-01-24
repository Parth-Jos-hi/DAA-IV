'''Question:- Given an array of nonnegative integers, design a linear algorithm
              and implement it using a program to find whether given key element is
              present in the array or not. Also, find total number of comparisons for each input case. 
              (Time Complexity = O(n), where n is the size of input)'''

def linear_search(arr,key):
    comparisons = 0

    for value in arr:
        comparisons += 1
        if value == key:
            return True,comparisons
    return False,comparisons
    
test_cases = int(input("Enter number of test Cases: ").strip())

while test_cases>0:
    n = int(input("Enter the size of array: ").strip())
    arr = list(map(int,input("Enter array elements: ").split()))
    key = int(input("Enter key element: ").strip())

    is_present,comparisons = linear_search(arr,key)

    if is_present:
        print("Present",comparisons)
    else:
        print("Not Present",comparisons)
         
    test_cases -= 1     

