import math
'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        '''
        :type s : List[str]
        :rtype : str
        '''
        def prefix(strs, index):
            check_prefix = strs[0][:index]
            for index in range(1, len(strs)):
                if not strs[index].startswith(check_prefix):
                    return False
            return True

        if not strs:
            return "" 

        minilength = float('inf') 
        for string in strs:
            minilength = min(minilength, len(string))

        low, high = 0, minilength

        while low <= high:
            mid = int((low + high)/2)
            if (prefix(strs, mid)):
                low = mid + 1
            else:
                high = mid - 1

        return strs[0][:math.floor((low+high)/2)]   

strs = ["flower","flow","floor"]

apt = Solution()
res = apt.longestCommonPrefix(strs) 
print(res)

