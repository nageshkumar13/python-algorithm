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


class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if len(str1) > len(str2):
            str1, str2 = str2, str1
        # Swap str1 and str2 if str2 is longer
        
        l_str1 = len(str1)
        for index in range(1, len(str1)+1):
            # Iterate over all possible lengths of substrings of str1
            if l_str1 % index != 0:
                continue
            # Check if the length of str1 is divisible by the current index
            
            size_to_take = int(l_str1 / index)
            # Calculate the size of substrings to take
            substr1 = str1[:size_to_take]
            # Extract substring from str1
            
            substr2 = str2
            # Initialize substr2 with str2
            
            while substr1 == substr2[:size_to_take]:
                substr2 = substr2[size_to_take:]
                # Check if the substrings match, if so, remove matched part from substr2
            
            if substr2 == "":
                return substr1
            # If substr2 becomes empty after all matches, return substr1
        return ""
        # If no common divisor found, return empty string

apt = Solution()
print(apt.gcdOfStrings(str1 = "AAAAA", str2 = "AA"))