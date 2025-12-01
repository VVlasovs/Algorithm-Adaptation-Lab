arr7 = [("Latvia", 300), ("Lithuania", 100), ("Latvia", 200)]

x = len(arr7)

for i in range(x):
    for j in range(0, x - 1):

        if arr7[j][0] > arr7[j + 1][0]:
            arr7[j], arr7[j + 1] = arr7[j + 1], arr7[j]
            
        elif arr7[j][0] == arr7[j + 1][0] and arr7[j][1] < arr7[j + 1][1]:
            arr7[j], arr7[j + 1] = arr7[j + 1], arr7[j]

print(arr7)


