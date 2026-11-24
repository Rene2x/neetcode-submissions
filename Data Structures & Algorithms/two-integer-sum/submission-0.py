class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force method
        # nested loops
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                # with indexes i and j we figure out if out target is reachable
                if nums [i] + nums[j] == target:
                    # if target is found, return the indexes that provided the target anwer
                    return [i,j]
        # if no target value is found, just return an empty List
        return []
        