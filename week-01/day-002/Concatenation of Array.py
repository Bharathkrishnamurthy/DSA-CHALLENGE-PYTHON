class Solution(object):
    def getConcatenation(self, nums):
        res=[]
        res.extend(nums)
        for i in range(len(nums)):
            res.append(nums[i])
    
        return res

    #   time and space=O(n)
