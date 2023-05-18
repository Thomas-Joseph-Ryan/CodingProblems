class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        num_uniq = 1
        last_uniq_index = 0
        current_uniq_num = nums[0]
        
        for index, num in enumerate(nums):
            if num == current_uniq_num:
                if index == 0:
                    continue
                nums[index] = "_"
            elif num != current_uniq_num:
                nums[last_uniq_index + 1] = num
                last_uniq_index += 1
                num_uniq += 1
                current_uniq_num = num
        return num_uniq