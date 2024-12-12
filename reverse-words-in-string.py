#Given an input string s, reverse the order of the words.
#A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
#Return a string of the words in reverse order concatenated by a single space.
#Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """


        # Step 1: Trim leading and trailing spaces and split the string into words
        words = s.strip().split()

        # Step 2: Reverse the list of words
        words.reverse()

        # Step 3: Join the reversed words with a single space
        return " ".join(words)

        