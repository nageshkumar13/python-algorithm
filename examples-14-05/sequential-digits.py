'''
    Given a range [low, high], return a list of all sequential digits that are in this range.
        
    For example:
    Input: low = 1000, high = 5000
    Output: [1234, 2345, 3456, 4567]
    Explanation: Numbers in the range [1000,5000] that have sequential digits are 1234, 2345, 3456, and 4567.
        
'''

class Solution(object):
    def sequentialDigits(self, low, high):
        '''        
        :type low : int
        :type high: int 
        :rtype : List[int]
        '''

        # Initialize an empty list to store the sequential digits
        result = []
        
        # Extract the first digit from the low input
        start = int(str(low)[0])
        
        # Iterate through the digits of the low input to construct the starting number
        for val in range(1, len(str(low))):
            new_val = start % 10 + 1  # Extract the last digit and add 1 to get the next digit
            start = start * 10 + new_val  # Append the next digit to the number
        
        # If the starting number is greater than the high input, return empty list
        if start > high:
            return result
        
        # Add the starting number to the result list
        result.append(start)

        # Loop until the last element in the result list is less than or equal to the high input
        while result[-1] <= high:
            temp = str(result[-1])  # Convert the last element in the result list to a string
            next_elem = int(temp[-1]) + 1  # Extract the last digit and add 1 to get the next digit
            
            # If the next digit is greater than 9, construct the next sequential number accordingly
            if next_elem > 9:
                next_greater = 0
                for index in range(len(temp) + 1):
                    next_greater = next_greater * 10 + (index + 1)
            else:
                next_greater = int(temp[1:]) * 10 + next_elem  # Construct the next sequential number
            
            # If the next sequential number is within the range, add it to the result list
            if next_greater <= high:
                result.append(next_greater)
            else:
                break  # Break the loop if the next sequential number exceeds the high input

        # Initialize an empty list to store the final result after filtering out unwanted numbers
        final_result = []
        
        # Filter out numbers containing '0' and numbers less than the low input
        for val in result:
            if '0' not in str(val) and val >= low:
                final_result.append(val)

        return final_result        
    
apt = Solution()

a = 10
b = 50

print(apt.sequentialDigits(a, b))
