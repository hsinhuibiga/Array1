#Reverse Words in a String III

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(map(lambda x : x[::-1], s.split(" ")))