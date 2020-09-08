class Solution(object):
    def twosum(self, nums, target):
        length = len(nums)
        for i in range(0, length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]
