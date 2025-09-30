def vigenere_cipher_encrypt(plain_text, keyword):
    encrypted_text = ""
    # 키워드를 모두 소문자로 변환해서 키 값으로 사용
    keyword = keyword.lower()
    keyword_len = len(keyword)
    keyword_idx = 0
    
    for char in plain_text:
        if 'a' <= char <= 'z':
            # 키워드 문자를 숫자로 변환 (a=0, b=1, ...)
            key_shift = ord(keyword[keyword_idx % keyword_len]) - ord('a')
            
            # 시저 암호처럼 적용
            encrypted_char_code = (ord(char) - ord('a') + key_shift) % 26 + ord('a')
            encrypted_text += chr(encrypted_char_code)
            
            # 알파벳만 키워드 인덱스를 증가
            keyword_idx += 1
        elif 'A' <= char <= 'Z':
            key_shift = ord(keyword[keyword_idx % keyword_len]) - ord('a')
            
            encrypted_char_code = (ord(char) - ord('A') + key_shift) % 26 + ord('A')
            encrypted_text += chr(encrypted_char_code)
            
            keyword_idx += 1
        else:
            encrypted_text += char # 알파벳이 아닌 겨웅 그대로 유지
    return encrypted_text

def vigenere_cipher_decrypt(cipher_text, keyword):
    decrypted_text = ""
    # 키워드를 모두 소문자로 변환해서 키 값으로 사용
    keyword = keyword.lower()
    keyword_len = len(keyword)
    keyword_idx = 0
    
    for char in cipher_text:
        if 'a' <= char <= 'z':
            key_shift = ord(keyword[keyword_idx % keyword_len]) - ord('a')
            
            # 복호화된 키 시프트를 빼는 방식
            decrypted_char_code = (ord(char) - ord('a') + key_shift) % 26 + ord('a')
            decrypted_text += chr(decrypted_char_code)
            
            # 알파벳만 키워드 인덱스를 증가
            keyword_idx += 1
        elif 'A' <= char <= 'Z':
            key_shift = ord(keyword[keyword_idx % keyword_len]) - ord('a')
            
            decrypted_char_code = (ord(char) - ord('A') + key_shift) % 26 + ord('A')
            decrypted_text += chr(decrypted_char_code)
            
            keyword_idx += 1
        else:
            decrypted_text += char # 알파벳이 아닌 겨웅 그대로 유지
    return decrypted_text

# === 예제 사용 ===

plain_text = "Attack at dawn"
encryption_keyword = "lemon" # 키워드

print(f"평문 : {plain_text}")
print(f"키워드 : {encryption_keyword}")

# 암호화
cipher_text = vigenere_cipher_encrypt(plain_text, encryption_keyword)
print(f"암호화된 텍스트 : {cipher_text}")

# 복호화
decrypted_text = vigenere_cipher_decrypt(cipher_text, encryption_keyword)
print(f"복호화된 텍스트 : {decrypted_text}")

print("\n===다른 예시===")
plain_text_2 = "Cryptography is an interesting field"
encryption_keyword_2 = "security"

print(f"평문 : {plain_text_2}")
print(f"키워드 : {encryption_keyword_2}")

# 암호화
cipher_text_2 = vigenere_cipher_encrypt(plain_text_2, encryption_keyword_2)
print(f"암호화된 텍스트 : {cipher_text_2}")

# 복호화
decrypted_text_2 = vigenere_cipher_decrypt(cipher_text_2, encryption_keyword_2)
print(f"복호화된 텍스트 : {decrypted_text_2}")