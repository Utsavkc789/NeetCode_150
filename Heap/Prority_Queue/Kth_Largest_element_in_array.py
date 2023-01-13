"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5


Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k
        def quickSelect(l,r):
            pivot, p = nums[r],l
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[p],nums[i] = nums[i],nums[p]
                    p += 1
            nums[p],nums[r] = pivot,nums[p]

            if p > k: return quickSelect(l,p-1)
            elif p < k: return quickSelect(p+1,r)
            else: return nums[p]
        return quickSelect(0,len(nums)-1)

