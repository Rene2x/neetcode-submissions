class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # puts the int list in numerical order | Both ways work well
        nums.sort()
        # start the for loop going through nums[], starting index is 1, not 0 so i-1 can exist 
        for i in range(1, len(nums)):
            # if our current index matches our previous index return True
            # Checking for neighbors
            if nums[i] == nums[i - 1]:
                return True
        # if not, return False
        return False
        
        