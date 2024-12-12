#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
#Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
#Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
#Return k.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0  # Handle empty list case

        k = 1  # Start with the first unique element
        
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:  # Compare with the last unique element
                nums[k] = nums[i]  # Place the unique element at the k-th position
                k += 1  # Move to the next position for unique elements
        
        return k  # Return the count of unique elements

        