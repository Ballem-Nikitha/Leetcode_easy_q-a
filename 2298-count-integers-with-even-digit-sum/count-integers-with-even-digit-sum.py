class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
    
        c=0
        for i in range(1,num+1):
            digit_sum=sum(int(j) for j in str(i))
            if digit_sum%2==0:
                c+=1
        return c
        """
        c=0
        for i in range(1,num+1):
            if i<=9 and i%2==0:
                c+=1
            if i >9:
                digit_sum=0
                for j in str(i):
                    digit_sum+=int(j)
                if digit_sum%2==0:
                    c+=1
        return c