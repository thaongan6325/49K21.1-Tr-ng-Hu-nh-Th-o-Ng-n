from typing import List

p = 17
q = 23
e = 5

PLAINTEXT = "Trương Huỳnh Thảo Ngân"

def egcd(a: int, b: int):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def modinv(a: int, m: int) -> int:
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError(f"Không tồn tại nghịch đảo modulo của {a} mod {m}")
    return x % m

def encrypt_bytes(data: bytes, e: int, n: int) -> List[int]:
    return [pow(b, e, n) for b in data]

def decrypt_bytes(cipher: List[int], d: int, n: int) -> bytes:
    return bytes([pow(c, d, n) for c in cipher])

if __name__ == "__main__":
    n = p * q 
    phi = (p - 1) * (q - 1)  
    d = modinv(e, phi)  

    print(f"Các tham số:\n  p = {p}\n  q = {q}\n  n = p*q = {n}\n  phi = {phi}\n  e = {e}\n  d (số mũ bí mật) = {d}\n")

    pt_bytes = PLAINTEXT.encode("utf-8")
    print(f"Thông điệp gốc (dạng byte UTF-8): {list(pt_bytes)}")

    ciphertext = encrypt_bytes(pt_bytes, e, n)
    print(f"Bản mã (danh sách số nguyên):\n{ciphertext}\n")

    recovered = decrypt_bytes(ciphertext, d, n)
    recovered_text = recovered.decode("utf-8")
    print(f"Bản giải mã (dạng byte): {list(recovered)}")
    print(f"Thông điệp giải mã: {recovered_text}\n")