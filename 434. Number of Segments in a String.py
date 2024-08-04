
"""
434. Number of Segments in a String

Given a string s, return the number of segments in the string.

A segment is defined to be a contiguous sequence of non-space characters.

Example 1:

Input: s = "Hello, my name is John"
Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
Example 2:

Input: s = "Hello"
Output: 1
"""

class Solution(object):
    def countSegments(self, s):
        if len(s.strip()) == 0:
            return 0
        s=s.strip()
        segment=s.split(' ')
        if '' in segment:
            coun=segment.count('')
            length=len(segment)-coun   
        else:
            length=len(segment)
        return length
        