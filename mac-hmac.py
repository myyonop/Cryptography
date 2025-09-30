from cryptography.hazmat.primitives import hashes, hmac
from cryptography.exceptions import InvalidSignature

# 1. HMAC 생성 (송신자)
key = 'supersecretkey8792873493'.encode('utf-8')
message = 'message authencication code test. 메시지 인증 코드 테스트'

h = hmac.HMAC(key, hashes.SHA256())
h.update(message.encode('utf-8'))
signature = h.finalize()
print('Key : ', key)
print('Message : ', message)
print('HMAC : ', signature.hex())
# 송신자 -> 수신자 (message, signature)

# 2. HMAC 검증
key = 'supersecretkey8792873493'.encode('utf-8')
try: 
    h = hmac.HMAC(key, hashes.SHA256())
    h.update(message.encode('utf-8'))
    h.verify(signature)
    print("\n검증 성공")
except InvalidSignature:
    print("\n검증 실패 : 서명이 유효하지 않습니다.")