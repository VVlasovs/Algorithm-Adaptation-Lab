arr6 = [(101, 85), (102, 70), (103, 95)]

x = len(arr6)
for i in range(x):
    for j in range(0, x -1):
        if arr6[j][1] < arr6[j + 1][1]:  
            arr6[j], arr6[j + 1] = arr6[j + 1], arr6[j]
print(arr6)


