class Solution(object):
    def removeOuerParentheses(self, S):
        '''
        :type S : str
        :rtype  : str
        '''
        temp, result = "", ""

        start_bracket = 0
        for char in S :
            temp += char
            if char == "(":
                start_bracket += 1
            else: 
                start_bracket -= 1
            if start_bracket == 0:
                result += temp[1:-1] 
                temp = ""  
        return result          

s = "(())(()()())()))"

apt = Solution()
res = apt.removeOuerParentheses(s)
print(res)


