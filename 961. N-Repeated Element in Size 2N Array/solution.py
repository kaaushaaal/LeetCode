class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        for i in nums:
            if i in seen:
                return i
            seen.add(i)

