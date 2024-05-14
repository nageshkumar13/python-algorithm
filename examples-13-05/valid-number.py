# Check if the given string is numeric.

class Solution(object):
    def isNumber(self, s):
        '''
        :type s : str 
        :rtype : bool 
        '''
        # Remove leading and trailing whitespace
        s = s.strip()
        try: 
            # Attempt to convert the string to float or int
            if isinstance(float(s), float) or isinstance(int(s), int):
                return True
        except Exception as e:
            # If conversion fails, return False
            return False
        
# Get user input
s = input("Give input an input : ")   

# Create an instance of Solution class
apt = Solution()

# Check if the input is a number
res = apt.isNumber(s)

# Print the result
if res :
    print(f"{s} is a number.") 
else:
    print(f"{s} is not a number")
