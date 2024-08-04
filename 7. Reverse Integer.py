# -*- coding: utf-8 -*-
"""
7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit 
integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers 
(signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
"""

#python:

    
class Solution(object):
    def reverse(self,x):
        reverse=0
        remainder=0
        ul=2**31-1
        ll=-2**31
        if x>0:
            while x>0:
                remainder=x%10
                reverse=reverse*10+remainder
                x=x//10
        elif x<0:
            x=abs(x)
            while x>0:
                remainder=x%10
                reverse=reverse*10+remainder
                x=x//10
            reverse=-reverse
        else:
            pass
        if ul>reverse>ll:
            return reverse
        else:
            return 0
        