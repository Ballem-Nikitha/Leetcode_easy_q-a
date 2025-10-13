class Solution(object):
    def canAliceWin(self, nums):
        sum1=0
        sum2=0
        for i in nums:
            if i>9:
                sum2+=i
            else:
                sum1+=i
        if sum1==sum2:
            return False
        return True