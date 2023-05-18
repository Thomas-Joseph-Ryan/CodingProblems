class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # There is probably a way to do it like this, but instead I
        # will try with O(1) space complexity
        # nums_copy = nums[:]
        # for index, num in enumerate(nums_copy):
        #     if index + k < len(nums) - 1:
        #         nums[index + k] = num
        #     else:
        #         nums[index + k - len(nums)] = num

        if len(nums) == 1:
            return
        next_num = None
        for rotation_step in range(k):
            current_num = nums[0]
            for index, num in enumerate(nums):
                next_index = (index + 1) % len(nums)
                next_num = nums[next_index]
                nums[next_index] = current_num
                current_num = next_num
            

# if __name__ == "__main__":
#     sol = Solution
#     ls = [1, 2, 3]
#     sol.rotate(sol, ls, 2)
#     print(ls)


