"""
258. Add Digits
Solved
Easy
Topics
Companies
Hint
Given an integer num, repeatedly add all its digits until the result has 
only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
 
"""

class Solution(object):
    def addDigits(self, num):
        if num==0:
            sum=0
        elif num%9==0:
            sum=9
        elif num%9!=0:
            sum=num%9
        else:
            pass
        return sum
        