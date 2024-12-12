#Find the minimum number of characters that must be flipped in a binary string such that the string can be divided into non-overlapping, even-length substrings, where each substring contains only 1s or 0s.


def getMinFlips(pwd: str) -> int:
    flips = 0
    # Iterate over the string in steps of 2 (pairs)
    for i in range(0, len(pwd), 2):
        # Compare the two characters in each pair
        if pwd[i] != pwd[i + 1]:
            # If characters are different, one flip is needed
            flips += 1
    return flips

# Sample input
pwd = "1110011000"
# Output the result
print(getMinFlips(pwd))  # Expected output: 3
