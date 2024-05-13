# Check if the given string is numeric.

class Solution(object):
    def isNumber(self, s):
        '''
        :type s : str 
        :rtype : bool 
        '''
        s = s.strip()
        try: 
            if isinstance(float(s), float) or isinstance(int(s), int):
                return True
        except Exception as e:
            return False
        
s = input("Give input an input : ")   

apt = Solution()
res = apt.isNumber(s)

if res :
    print(f"{s} is a number.") 
else:
    print(f"{s} is not a number")