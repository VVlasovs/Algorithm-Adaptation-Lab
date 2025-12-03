arr3 = ["Melon", "Apple", "Zebra", "Grape"]

for i in range(len(arr3)): 
    min_index = i 
    for j in range(i + 1, len(arr3)):
        if arr3[j] < arr3[min_index]:
            min_index = j 
    
    arr3[i], arr3[min_index] = arr3[min_index], arr3[i]

print(arr3)
