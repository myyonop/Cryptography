def atbash_cipher(text):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            result += chr(ord('Z') - (ord(char) - ord('A')))
        elif 'a' <= char <= 'z':
            result += chr(ord('z') - (ord(char) - ord('a')))
        else:
            result += char
    return result

# ===예제 사용===
plain_text = "Hello, Atbash!"
cipher_text = atbash_cipher(plain_text)
decrypted_text = atbash_cipher(cipher_text)  # 같은 함수로 복호화

print(f"평문: {plain_text}")
print(f"암호문: {cipher_text}")
print(f"복호화: {decrypted_text}")
