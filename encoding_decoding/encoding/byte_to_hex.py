# 바이트 배열
bytes_object = b'\xec\x95\x88\xeb\x85\x95\xed\x95\x98\xec\x84\xb8\xec\x9a\x94'

# 바이트 배열을 16진수 문자열로 변환
hex_string = bytes_object.hex()
print(hex_string)

# 공백 추가
hex_string_spaced = ' '.join([f'{b:02x}' for b in bytes_object])
print(hex_string_spaced)
