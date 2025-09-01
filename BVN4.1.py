def ma_hoa_caesar(plaintext, k):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            ciphertext += chr((ord(char) - shift + k) % 26 + shift)
        else:
            ciphertext += char
    return ciphertext


if __name__ == "__main__":
    k = 30   # STT = 30
    plaintext = "Truong Huynh Thao Ngan"
    ciphertext = ma_hoa_caesar(plaintext, k)

    print("TenCuaBan :", plaintext)
    print("STT (k) :", k)
    print("Ciphertext:", ciphertext)
