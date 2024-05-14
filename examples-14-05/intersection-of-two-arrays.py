'''
	Given two arrays, write a function to compute their intersection.

	Example:
	Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

	Note:
	Each element in the result should appear as many times as it shows in both arrays.
	The result can be in any order.
	Follow up:
	What if the given array is already sorted? How would you optimize your algorithm?
	What if nums1's size is small compared to nums2's size? Which algorithm is better?
	What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
'''

class Solution(object):
    def intersect(self, num1, num2):

        '''
        type num1 : List[int]
        type num2 : List[int]
        rtype     : List[int]
        '''
        num2.sort()
        num1.sort()

        i,j = 0,0
        result = [] 
        while i < len(num1) and j < len(num2):
            if num1[i] == num2[j]:
                result.append(num1[i])
                i += 1
                j += 1
            elif num1[i] > num2[j]:
                j += 1
            else :
                i += 1 
        return result

a = [1, 5, 2, 9]
b = [2, 7, 1, 6]
apt = Solution()
res = apt.intersect(a,b)

print(res)



            
            




