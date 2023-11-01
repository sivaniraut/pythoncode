"""Input: a2b3f5k1

Output: aabbbfffffk"""

def decode_string(s):
    result = []
    i = 0

    while i < len(s):
        char = s[i]
        i += 1

        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        result.append(char * num)

    return ''.join(result)

input_str = "a2b3f5k1"
output_str = decode_string(input_str)
print(output_str)
