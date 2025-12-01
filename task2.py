
arr2 = [5, 1, 4, 2, 8]
swaps = 0 

for i in range(len(arr2)-1):
    swapped = False
    for j in range(len(arr2)-1):
        if arr2[j] < arr2[j+1]:
            arr2[j], arr2[j+1] = arr2[j+1], arr2[j]
            swapped = True 
            swaps += 1
    if not swapped: 
        break 
print("Amount of swaps:", swaps)

