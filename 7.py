'''
Problem 2: Contains Duplicate
Question : nums = [1,2,3,1]

Output:
True

Because 1 appears twice.
'''

class Solution:
    def constarintDuplication(self,nums):

        seen = set()

        for num in nums:
         
            if num in seen:
                return True
            seen.add(num)

        return False