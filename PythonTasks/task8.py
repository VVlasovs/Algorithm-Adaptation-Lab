arr8 = [5, -2, 8, -5, 10, 0, -10]

for i in range(len(arr8)):
    swapped = False
    for j in range(len(arr8) - 1):
        if arr8[j] >= 0 and arr8[j + 1] < 0:
            arr8[j], arr8[j + 1] = arr8[j + 1], arr8[j]
            swapped = True
    if not swapped:
        break

print(arr8)

