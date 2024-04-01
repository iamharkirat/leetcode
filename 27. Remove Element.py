def removeElement(nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k, nums

nums = [3,2,2,3]
k, nums = removeElement(nums, 3)

print(k, nums)