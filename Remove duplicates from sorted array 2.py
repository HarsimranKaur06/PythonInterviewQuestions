#Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.
#Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
#Return k after placing the final result in the first k slots of nums.
#Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) <= 2:
            return len(nums)  # If the length is 2 or less, no need to remove anything

        k = 2  # We can keep up to 2 duplicates, starting from the third element

        for i in range(2, len(nums)):
            # Check if the current element is different from the element at index k-2
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]  # Place the current element at the k-th position
                k += 1  # Increment the count of unique elements allowed

        return k  # Return the length of the modified array
