'''
	Given an integer, write a function to determine if it is a power of three.

	Follow up:
	Could you do it without using any loop / recursion?
'''

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
        	return False

        import math
        return (math.log10(n)/math.log10(3))%1 == 0

n = int(input("Give any number :"))

apt = Solution() 
res = apt.isPowerOfThree(n)

if res:
    print(f"{n} is a power of 3.")
else:
    print(f"{n} is not a power of 3.")
