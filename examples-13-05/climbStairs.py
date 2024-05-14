# Introduction:
# This program calculates the number of distinct ways to climb a staircase of n steps, 
# where at each step, you can either climb 1 or 2 steps.

class Solution(object):
    def climbStairs(self, n):
        '''
        Function to calculate the number of distinct ways to climb a staircase of n steps.
        
        :param n: int, the number of steps in the staircase.
        :return: int, the number of distinct ways to climb the staircase.
        '''
        # If there are no steps, there is only one way to climb, i.e., not climbing at all.
        if n == 0: 
            return 0
        
        # Initialize an array to store the number of distinct ways to reach each step.
        dp = [0] * n
        
        # Base cases: There is only one way to reach the first and second steps respectively.
        dp[0], dp[1] = 1, 2

        # Iterate through the steps starting from the third step.
        for index in range(2, n):
            # The number of ways to reach the current step is the sum of ways to reach the previous two steps.
            dp[index] = dp[index - 1] + dp[index - 2]

        # Return the number of distinct ways to reach the nth step.
        return dp[n - 1]

# Ask user for the number of stairs.
nu_of_steps = int(input("Give the number of stairs: "))        

# Create an instance of the Solution class.
apt = Solution()

# Print the number of distinct ways to climb the given number of stairs.
print(apt.climbStairs(nu_of_steps))
