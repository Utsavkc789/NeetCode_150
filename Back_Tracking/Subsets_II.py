"""
Given an integer array nums that may contain duplicates, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

"""

# TC O(2^N)

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backTrack(i,subsets):
            if i == len(nums):
                res.append(subsets[::])
                return

            #decision to include nums[i]
            subsets.append(nums[i])
            backTrack(i+1,subsets)

            #decision to not include nums[i]
            subsets.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1    
            backTrack(i+1,subsets)

        backTrack(0,[])
        return res
