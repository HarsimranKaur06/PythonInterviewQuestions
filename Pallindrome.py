#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#Given a string s, return true if it is a palindrome, or false otherwise.

 


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Convert to lowercase and filter only alphanumeric characters
        filtered_string = ''.join(char.lower() for char in s if char.isalnum())
        
        # Check if the filtered string is the same when reversed
        return filtered_string == filtered_string[::-1]
