# This class provides a solution to add two binary numbers represented as strings.
class Solution(object):
    def addBinary(self, a, b):
        # Initialize an empty string to store the result.
        result = ""
        # Initialize a variable to keep track of the carry.
        carry = 0
        # Initialize indices to traverse both input strings from right to left.
        index_a, index_b = len(a) - 1, len(b) - 1

        # Iterate through both binary strings until one of them is fully processed.
        while index_a >= 0 or index_b >= 0:
            # Initialize the sum with the current value of carry.
            sum_val = carry
            # Add the corresponding digits from both strings if they are available.
            if index_a >= 0:
                sum_val += int(a[index_a])
                index_a -= 1
            if index_b >= 0:
                sum_val += int(b[index_b])
                index_b -= 1

            # Append the least significant digit of the sum to the result.
            result = str(sum_val % 2) + result
            # Update the carry for the next iteration.
            carry = sum_val // 2

        # If there is a carry after processing all digits, append it to the result.
        if carry:
            result = '1' + result

        # Return the final result.
        return result

# Example usage:
if __name__ == "__main__":
    # Binary numbers to add
    a = "10110"
    b = "01101"
    
    # Create an instance of the Solution class
    atp = Solution()
    
    # Perform binary addition
    result_binary = atp.addBinary(a, b)
    
    # Convert binary result to decimal
    result_decimal = int(result_binary, 2)
    
    # Print the binary and decimal values of the result
    print("Binary:", result_binary)
    print("Decimal:", result_decimal)
