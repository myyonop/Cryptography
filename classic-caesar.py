def caesar_cipher_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if 'a' <= char <= 'z': #소문자인 경우
            start = ord('a')
            encrypted_char_code = (ord(char) - start + key) % 26 + start
            encrypted_text += chr(encrypted_char_code)
        elif'A' <= char <= 'Z': #대문자인 경우
            start = ord('A')
            encrypted_char_code = (ord(char) - start + key) % 26 + start
            encrypted_text += chr(encrypted_char_code)
        else: # 알파벳이 아닌 경우 (공백, 숫자, 특수문자 등)
            encrypted_text += char # 그대로 유지
    return encrypted_text

def caesar_cipher_decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if 'a' <= char <= 'z':
            start = ord('a')
            decrypted_char_code = (ord(char) - start - key) % 26 + start
            decrypted_text += chr(decrypted_char_code)
        elif 'A' <= char <= 'Z':
            start = ord('A')
            decrypted_char_code = (ord(char) - start - key) % 26 + start
            decrypted_text += chr(decrypted_char_code)
        else:
            decrypted_text += char
    return decrypted_text

plain_text = "Hello, Caesar Cipher!"
encryption_key = 3 # key를 3으로 설정

#암호화
cipher_text = caesar_cipher_encrypt(plain_text, encryption_key)
print(f"평문 : {plain_text}")
print(f"암호화된 텍스트 : {cipher_text}")

#복호화
decrypted_text = caesar_cipher_decrypt(cipher_text, encryption_key)
print(f"복호화된 텍스트 : {decrypted_text}")

#다른 키로 시도
print("\n--- 다른 키로 암호화 시도---")
plain_text_2 = "Python"
encryption_key_2 = 10

#암호화
cipher_text_2 = caesar_cipher_encrypt(plain_text_2, encryption_key_2)
print(f"평문 : {plain_text_2}")
print(f"암호화된 텍스트 : {cipher_text_2}")

#복호화
decrypted_text_2 = caesar_cipher_decrypt(cipher_text_2, encryption_key_2)
print(f"복호화된 텍스트 : {decrypted_text_2}")