class Solution(object):
    def differenceOfSums(self, n, m):
        sum1 = sum([i for i in range(1, n + 1) if i % m != 0])
        sum2 = sum([i for i in range(1, n + 1) if i % m == 0])
        return sum1 - sum2
