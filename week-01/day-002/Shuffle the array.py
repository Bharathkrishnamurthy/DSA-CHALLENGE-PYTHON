class Solution(object):
    def shuffle(self, nums, n):
        res=[]
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res
# Time Complexity: O(n)
# Space Complexity: O(n)
