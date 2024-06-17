
class Solution(object):
        def minAbsoluteDiff(self, a):          
            
            a = list(set(a))
            a.sort()

            mindiff = a[1] - a[0]

            for i in range(2, len(a)):
                mindiff = min(mindiff, (a[i] - a[i-1]))

            result = []

            for i in range(1, len(a)):
                if mindiff == a[i] - a[i-1]:
                    result.append([a[i-1],a[i]])

            return result


l_array = [1,2,9,0,76,3,23,4,2,5, 6, 3, -1]     
apt = Solution()

print(apt.minAbsoluteDiff(l_array))