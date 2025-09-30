import base64
import os
from cryptography.hazmat.primitives import poly1305
from cryptography.exceptions import InvalidSignature

# 1. MAC 생성
key = os.urandom(32)
message = 'Message to authenticate 메시지 인증 코드 테스트'
p = poly1305.Poly1305(key)
p.update(message.encode('utf-8'))
signature = p.finalize()
print('Key : ', base64.b64encode(key).decode())
print('Message : ', message)
print('Mac : ', signature.hex())

# 2. MAC 검증
try:
    p = poly1305.Poly1305(key)
    p.update(message.encode('utf-8'))
    p.verify(signature)
    print("\n검증 성공")
except InvalidSignature:
    print("\n검증 실패 : 서명이 유효하지 않습니다.")