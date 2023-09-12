hex_string = "EC 95 88 EB 85 95 ED 95 98 EC 84 B8 EC 9A 94"
bytes_object = bytes.fromhex(hex_string)

# UTF-8 디코딩
try:
    utf8_string = bytes_object.decode("utf-8")
    print(utf8_string)
except UnicodeDecodeError:
    print("The byte sequence could not be decoded with UTF-8.")
