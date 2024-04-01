nums = [0,0,1,1,1,2,2,3,3,4]

def removeDuplicates(nums):
    length = len(nums)
    write_index = 1
    
    for read_index in range(1, length):
        if nums[read_index] != nums[read_index - 1]:
            nums[write_index] = nums[read_index]
            write_index += 1

    for i in range(write_index, length):
        nums[i] = '_'

    return write_index, nums

nums, list = removeDuplicates(nums)
print(nums, list)

