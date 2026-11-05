class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)

        res=[0]*(m+n)

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                digit1=int(num1[i])
                digit2=int(num2[j])

                prod=digit1 * digit2 

                total=prod + res[i+j+1]

                res[i+j+1]=total%10
                res[i+j]+=total//10

        return ''.join(map(str, res)).lstrip('0')

# Time Complexity: O(m × n)
# Space Complexity: O(m + n)
