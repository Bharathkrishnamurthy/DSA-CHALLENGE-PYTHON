class Solution(object):
    def runningSum(self, nums):
        res=[]
        total=0
        for i in range(len(nums)):
            total+=nums[i]
            res.append(total)
            
        return res
        

# Time Complexity: O(n)
# Space Complexity: O(n)
