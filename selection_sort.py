arr=[12,56,78,34,52,1]

for i in range(len(arr)):
    min_idx=i

    for j in range(min_idx,len(arr)):
        if arr[j]<arr[min_idx]:
            min_idx=j

    arr[i],arr[min_idx]=arr[min_idx],arr[i]

print(arr)