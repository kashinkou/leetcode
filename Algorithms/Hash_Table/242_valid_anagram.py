'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        counter = [0 for x in range(26)]
        for x in s:
            counter[ord(x) - ord('a')] += 1
        for x in t:
            counter[ord(x) - ord('a')] -= 1
            if counter[ord(x) - ord('a')] < 0:
                return False
        return True
        