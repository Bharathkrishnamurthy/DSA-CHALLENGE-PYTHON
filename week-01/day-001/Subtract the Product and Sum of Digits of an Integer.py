class Solution(object):
    def subtractProductAndSum(self, n):
        total=0
        prod=1
        res=0

        while n>0:

            digit=n%10

            prod*=digit
            total+=digit
            n=n//10
            res=prod-total
        return res

# time=O(logn)
# space=O(1)
        
