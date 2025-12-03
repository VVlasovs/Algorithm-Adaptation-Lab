arr4 = ["Melon", "Apple", "Zebra", "Grape"]

for i in range(1, len(arr4)):
        key = arr4[i]
        j = i - 1
        while j >= 0 and arr4[j] < key:  
            arr4[j + 1] = arr4[j]
            j -= 1
        arr4[j + 1] = key
print(arr4)



# for i in range(len(arr4)): 
#     min_index = i 
#     for j in range(i + 1, len(arr4)):
#         if arr4[j] > arr4[min_index]:
#             min_index = j                                Non Insert Version - Not Important 
    
#     arr4[i], arr4[min_index] = arr4[min_index], arr4[i]

# print(arr4)