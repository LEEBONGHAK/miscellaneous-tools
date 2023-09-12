# UTF-8 디코딩
encoded_string = b'\xec\x95\x88\xeb\x85\x95\xed\x95\x98\xec\x84\xb8\xec\x9a\x94'
decoded_string = encoded_string.decode("utf-8")
print(decoded_string)
