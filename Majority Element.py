#Given an array nums of size n, return the majority element.
#The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num  # Potential candidate for majority element
            count += (1 if num == candidate else -1)  # Increment or decrement count
            
        return candidate  # The candidate is the majority element