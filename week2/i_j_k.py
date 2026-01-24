arr = [1,2,3,4,5,6,6,7]
n = len(arr)
for k in range(n-1, 1, -1):
    sum = arr[k]
    i = 0
    j = k-1
    while(i < j):
        if(arr[i] + arr[j] > sum):
            j-= 1
        elif(arr[i] + arr[j] < sum):
            i += 1
        else:
            print(i,j,k)
            break
