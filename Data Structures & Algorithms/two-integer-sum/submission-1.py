class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # creating array copy
        A = []
        # iterate through nums[] and add to listA
        for i, num in enumerate(nums):
            # adding to the back of list A
            A.append([num, i])
        # sort the array
        A.sort()

        # initialize 2 pointers (i,j) to dettermine if sum of numbers equal target
        i, j = 0, len(nums) - 1
        while i < j:
            current = A[i][0] + A[j][0]
            if current == target:
                return [min(A[i][1], A[j][1]),
                        max(A[i][1], A[j][1])]
            elif current < target:
                i += 1
            else:
                j -= 1
        return []

       
       
       
       
       
       
       
       
       
        # brute force method
        # nested loops
    #    for i in range(len(nums)):
    #       for j in range(i+1, len(nums)):
                # with indexes i and j we figure out if out target is reachable
    #            if nums [i] + nums[j] == target:
                    # if target is found, return the indexes that provided the target anwer
    #                return [i,j]
        # if no target value is found, just return an empty List
    #    return []
        