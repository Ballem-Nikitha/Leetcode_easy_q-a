class Solution(object):
    def differenceOfSum(self, nums):
        sum1=0
        for i in nums:
            sum1+=i
        sum=0
        for i in nums:
            if len(str(i))>1:
                for j in str(i):
                    sum+=int(j)
            else:
                sum+=i
        return abs(sum1-sum)
        