class Solution(object):
    def twoSum(self, nums, target):
        seen = []
        len_lst = len(nums)

        for i in range(len_lst):
            if nums[i] in seen:
                continue
            else:
                for j in range(i+1, len_lst):
                    if nums[i] + nums[j] == target:
                        return [i, j]
            seen.append(nums[i])
