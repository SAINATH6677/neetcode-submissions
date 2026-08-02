class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        m=0
        for i in nums:
            if i == 1:
                m+=1
                count = max(count,m)
            else:
                m=0

        return count

        