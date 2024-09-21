# binary_string = "1011001100100010101001101110000111011010000000100110111000011000"
# decimal_number = int(binary_string, 2)
# hexadecimal_string = hex(decimal_number)
# print(hexadecimal_string)

def replace_byte(hex_string, position):
    byte_array = bytearray.fromhex(hex_string)
    for i in range(256):
        byte_array[position] = i
        print(byte_array.hex())
        
    
                        #f5cf17764cb71dbea07462c13a917686
hex_string = "aadf07665ca70daeb06472d12a81669603f0655cbf258fd96c5b10e87d20881f"
position = 0
result = replace_byte(hex_string, position)

result = 0xf5cf17764cb71dbea07462c13a917686 ^ 0xd5e7640f3fc378d3801007a34ff656e0
print(hex(result))

hex_string = "37326534316636396639373038343330202873797374656d2064656275672066"
byte_data = bytes.fromhex(hex_string)
print(byte_data)


