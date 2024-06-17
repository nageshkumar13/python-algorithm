'''
For strings S and T, we say "T divides S" if and only if S = T + ... + T 
(T concatenated with itself 1 or more times)
Return the largest string X such that X divides str1 and X divides str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
''' 

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcdOfStrings(str1, str2):
    # Find the gcd of the lengths of str1 and str2
    len1, len2 = len(str1), len(str2)
    gcd_len = gcd(len1, len2)
    
    # Candidate string that could be the gcd string
    candidate = str1[:gcd_len]
    
    # Check if this candidate divides both str1 and str2
    if candidate * (len1 // gcd_len) == str1 and candidate * (len2 // gcd_len) == str2:
        return candidate
    else:
        return ""

# Test cases
str1 = "AB"
str2 = "ABABAB"

print(gcdOfStrings(str1, str2))
