def cari_bilangan_cacah_terkecil(data):
    data_set = set(data)
    bilangan_cacah = min(data_set)
    while bilangan_cacah in data_set:
        bilangan_cacah += 1
    return bilangan_cacah

print ("Volem Alvaro Azira")
input1 = [5, 2, 8, 4, 3, 10]
output1 = cari_bilangan_cacah_terkecil(input1)
print("Output 1:", output1)

input2 = [2, 3, 4, 6]
output2 = cari_bilangan_cacah_terkecil(input2)
print("Output 2:", output2)

input3 = [8, 6, 7, 12]
output3 = cari_bilangan_cacah_terkecil(input3)
print("Output 3:", output3)
