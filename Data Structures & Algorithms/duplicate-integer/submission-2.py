class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # given nums[int]. True if any repeating value, False if none
        # sort nums
        nums.sort()
        
        # check neighbors
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
