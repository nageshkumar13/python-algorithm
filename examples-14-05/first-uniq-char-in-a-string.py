'''
	Given a string, find the first non-repeating character in it and return it's index. 
    If it doesn't exist, return -1.

	Examples:

	s = "leetcode"
	return 0.

	s = "loveleetcode",
	return 2.
'''

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1
    

istr = input("Give any string/word : ")
apt = Solution()

res = apt.firstUniqChar(istr)

if res >= 0:
    print(f"{istr[res]} is the first non repeating character in {istr}.")
else:
    print("All characters are repeated in the given string.")    
    