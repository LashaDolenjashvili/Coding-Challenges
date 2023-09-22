"""
CHALLENGE DESCRIPTION
- - - - - - - - - - - -
You're given a string like 'aaabbtggl'. 

You want to compress this string so that consecutive occurrences 
of the same character are represented as the character followed 
by the number of occurrences. 

The example transforms into 'a3b2t1g2l1'.
"""
def compress_string(s):
    # Check for an empty string
    if not s:
        return ""


    # Initialization
    compressed = []
    count = 1
    prev_char = s[0]


    # Loop through the string, starting 
    # from the second character
    for letter in s[1:]:
        if letter == prev_char:
            count += 1

        else:
            compressed.append(prev_char + str(count))
            prev_char = letter
            count = 1

    # Finalize the result
    compressed.append(prev_char + str(count))

    return ''.join(compressed)

# Test our function
s = 'aaabbtggl'
result = compress_string(s)
print(result)  # This should print: 'a3b2t1g2l1'
