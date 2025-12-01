arr5 = [7, 3, 5, 3, 1, 7]

x = len(arr5)

for i in range(x):
    min_index = i
    for j in range(i + 1, x):
        if arr5[j] < arr5[min_index]:
            min_index = j
    arr5[i], arr5[min_index] = arr5[min_index], arr5[i]
print(arr5)

# Ja divas vērtības ir vienādas, algoritms neizvēlas nevienu no tām kā
# mazāku vai lielāku un pārvieto tās atbilstoši to pozīcijai. Dublikāti tiek
# uzskatīti par normālām vērtībām, un skaitļu secība paliek nemainīga.