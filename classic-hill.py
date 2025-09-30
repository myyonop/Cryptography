import numpy as np

def text_to_numbers(text):
    return [ord(c) - ord('A') for c in text.upper() if c.isalpha()]

def numbers_to_text(nums):
    return ''.join(chr(n + ord('A')) for n in nums)

def hill_encrypt(plain_text, key_matrix):
    n = key_matrix.shape[0]
    nums = text_to_numbers(plain_text)
    
    # 패딩 처리
    while len(nums) % n != 0:
        nums.append(ord('X') - ord('A'))  # 'X'로 패딩
    
    nums = np.array(nums).reshape(-1, n).T
    encrypted = (np.dot(key_matrix, nums) % 26).T.flatten()
    return numbers_to_text(encrypted)

def hill_decrypt(cipher_text, key_matrix):
    n = key_matrix.shape[0]
    nums = text_to_numbers(cipher_text)
    nums = np.array(nums).reshape(-1, n).T

    # 역행렬 (mod 26) 구하기
    det = int(round(np.linalg.det(key_matrix))) % 26
    det_inv = pow(det, -1, 26)  # det의 모듈러 역원
    adjugate = np.round(det * np.linalg.inv(key_matrix)).astype(int) % 26
    inv_matrix = (det_inv * adjugate) % 26
    
    decrypted = (np.dot(inv_matrix, nums) % 26).T.flatten()
    return numbers_to_text(decrypted)

# 예시 키 행렬 (2x2)
key = np.array([[3, 3],
                [2, 5]])

plain_text = "HELLO"
cipher_text = hill_encrypt(plain_text, key)
decrypted_text = hill_decrypt(cipher_text, key)

print(f"평문: {plain_text}")
print(f"암호문: {cipher_text}")
print(f"복호화: {decrypted_text}")