#Given a string s consisting of words and spaces, return the length of the last word in the string.
#A word is a maximal substring consisting of non-space characters only.

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Remove any trailing spaces
        s = s.strip()
        
        # Split the string into words by spaces
        words = s.split(" ")
        
        # Return the length of the last word
        return len(words[-1])
