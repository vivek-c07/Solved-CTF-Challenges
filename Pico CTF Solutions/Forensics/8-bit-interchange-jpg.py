import hexdump

def modify_hex(hex_string):
    hexdump_array = [i for i in hex_string]
    s = ''
    temphex = []
    new_hexstring = ""
    for c, i in enumerate(hexdump_array):
        if i == ' ' or i == '\n':
            temphex.append(s)
            s = ''
        if len(temphex) == 4:
            temphex = temphex[::-1]
            for j in temphex:
                new_hexstring += j
            temphex = []
        s += i

    return new_hexstring

# Read hex data from a file
with open("challengefile", "rb") as f:
    hex_data = f.read()

# Convert bytes to a hex string
hex_string = hexdump.dump(hex_data)

modified_hex_string = modify_hex(hex_string)
print(modified_hex_string)

# Convert the modified hex string back to bytes
modified_data = bytes.fromhex(modified_hex_string.replace(" ", "").replace("\n", ""))

# Write the modified data back to the file
with open("modified_challengefile", "wb") as f:
    f.write(modified_data)
