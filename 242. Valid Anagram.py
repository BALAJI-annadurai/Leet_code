"""
242. Valid Anagram
Solved
Easy
Topics
Companies
Given two strings s and t, return true if t is an anagram of s, and false 
otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different 
word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""

class Solution(object):
    def isAnagram(self, s, t):
        new_s=list(s)
        new_t=list(t)
        new_s.sort()
        new_t.sort()
        s=''.join(new_s)
        t=''.join(new_t)
        if s==t:
            return True
        else:
            return False