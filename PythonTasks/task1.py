arr1 = [20, 5, 1, 8, 15, 3]

for i in range(len(arr1)-1):
    swapped = False
    for j in range(len(arr1)-1):
        if arr1[j] < arr1[j+1]:
            arr1[j], arr1[j+1] = arr1[j+1], arr1[j]
            swapped = True 
    if not swapped: 
        break 
print(arr1)



# for i in range(len(arr1)-1):
#     swapped = False
#     for j in range(len(arr1)-1):
#         if arr1[j] > arr1[j+1]:
#             arr1[j], arr1[j+1] = arr1[j+1], arr1[j]
#             swapped = True 
#     if not swapped: 
#         break 
#     arr1.sort(reverse=True)

# print("Array after pass:", arr1)
