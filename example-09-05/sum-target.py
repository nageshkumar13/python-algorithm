class Solution(object):
    def twoSum(self, nums, target):
        mapping = {}

        for index, val in enumerate(nums):
            diff = target - val
            if diff in mapping:
                return [index, mapping[diff]]
            else:
                mapping[val] = index
        return None  # Return None if no indices are found

solution = Solution()
indices = solution.twoSum(nums=[2, 7, 11, 15], target=17)

if indices is None:
    print("No indices found.")
else:
    index1, index2 = indices
    print(f"The indices {index1} and {index2} in the array give the sum equal to the target.")
