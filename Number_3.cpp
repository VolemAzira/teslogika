#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>

bool isPasswordValid(const char *password) {
    int length = strlen(password);
    
    // Cek panjang kata sandi
    if (length < 8 || length > 32) {
        printf("Kata sandi minimal 8 karakter dan maksimal 32 karakter\n");
        return false;
    }
    
    // Cek karakter awal
    if (isdigit(password[0])) {
        printf("Karakter awal tidak boleh angka\n");
        return false;
    }
    
    bool hasLower = false;
    bool hasUpper = false;
    bool hasDigit = false;
    
    // Cek karakter pada setiap posisi
    for (int i = 0; i < length; i++) {
        char ch = password[i];
        
        if (isdigit(ch))
            hasDigit = true;
        else if (islower(ch))
            hasLower = true;
        else if (isupper(ch))
            hasUpper = true;
    }
    
    // Cek persyaratan huruf kapital, huruf kecil, dan angka
    if (!hasLower || !hasUpper)
        printf("Harus memiliki huruf kapital dan huruf kecil\n");
    
    if (!hasDigit)
        printf("Harus memiliki angka\n");
    
    if (!hasLower || !hasUpper || !hasDigit)
        return false;
    
    // Kata sandi valid
    printf("Kata sandi valid\n");
    return true;
}

int main() {
    char password[50]; 
    bool isValid = false;
    
    do {
        printf("Masukkan kata sandi: ");
        scanf("%s", password);
        
        isValid = isPasswordValid(password);
        printf("\n");
    } while (!isValid);
    
    return 0;
}

