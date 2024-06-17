
class Solution(object):
    def even_degits(self, b):
        num_with_even_digits = 0
        for i in b:
            if len(str(i))%2 == 0:
                num_with_even_digits +=1
        return(num_with_even_digits)    


a = [12, 766, 2829, 11, 1]

apt = Solution()

print(apt.even_degits(a))