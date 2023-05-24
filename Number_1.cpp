#include <stdio.h>

void cetak(int N) {
    int count = 0;
    int i = 1;

    while (count < N) {
        if (i % 3 == 0 || i % 7 == 0) {
            if (i % 3 == 0 && i % 7 == 0) {
                printf("Z");
            } else {
                printf("%d", i);
            }
            count++;
            if (count != N) {
                printf(", ");
            }
        }
        i++;
    }
}

int main() {
    int N = 0;
    printf("Volem Alvaro Azira\n");
    printf("Masukkan Banyak Angka = ");
    scanf("%i",&N);

    printf("Output: ");
    cetak(N);

    return 0;
}

