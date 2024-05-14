# This class provides a solution to add one to a number represented as an array of digits.
class Solution(object):
    # Method to add one to the given list of digits.
    def plusone(self, digits):
        '''
        :type digits: List[int]    # Input: List of integers representing digits.
        :rtype: List[int]          # Output: List of integers representing the result.
        '''

        result = []  # Initialize an empty list to store the result.
        if not digits:  # Check if the input list is empty.
            return []  # If empty, return an empty list.

        carry = 1  # Set the carry to 1 initially since we're adding one.
        new_digits = digits[::-1]  # Reverse the list of digits.
        
        # Iterate through the reversed list of digits.
        for index in range(len(new_digits)):
            # Add the carry to the current digit and take modulo 10 to get the new digit.
            # Update the carry by integer division of the sum by 10.
            new_digits[index], carry = (new_digits[index] + carry) % 10, (new_digits[index] + carry) // 10

        # If there is still a carry after iterating through all digits, append it to the list.
        if carry > 0:
            new_digits.append(carry) 

        # Reverse the list of digits again to get the correct result.
        return new_digits[::-1] 


# Example usage:
k = [1, 5, 4, 2, 7]  # Example list of digits.
apt = Solution()  # Create an instance of the Solution class.
print(apt.plusone(k))  # Print the result of adding one to the list of digits.
