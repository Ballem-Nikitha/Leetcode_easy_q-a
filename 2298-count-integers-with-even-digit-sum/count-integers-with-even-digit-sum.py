class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        c=0
        for i in range(1,num+1):
            digit_sum=sum(int(j) for j in str(i))
            if digit_sum%2==0:
                c+=1
        return c