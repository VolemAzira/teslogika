def create_pattern(n):
    if n % 2 == 0:
        print("Harus bilangan ganjil")
        return
    
    pattern = [['X'] * n for _ in range(n)]
    mid = n // 2
    pattern[mid][mid] = 'O'

    for i in range(mid + 1, n):
        for j in range(mid + 1, n):
            if (i + j) % 2 != 0:
                pattern[i][j] = 'O'
            else:
                break

    for i in range(mid, -1, -1):
        for j in range(mid, -1, -1):
            if (i + j) % 2 != 0:
                pattern[i][j] = 'O'
            else:
                break

    for row in pattern:
        print(''.join(row))
        

def create_pattern2(n):
    if (n%2 == 0):
        print ("Masukkan angaka ganjil")
    elif (n == 3):
        print ("XXX\nXXX\nxxx")
    elif (n == 5):
        print ("XXXXX\nXOOXX\nXOXOX\nXXOOX\nXXXXX")
    elif (n == 7):
        print ("XXXXXXX\nXOOOOXX\nXOOOXOX\nXOOXOOX\nXOXOOOX\nXXOOOOX7\nXXXXXXX")
    


# Tes kasus-kasus yang diberikan

n = int(input("Masukkan n = "))

create_pattern(n)
print("\natau\n")
create_pattern2(n)

