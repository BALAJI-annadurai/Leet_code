# -*- coding: utf-8 -*-
"""
448. Find All Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not 
appear in nums.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        new_nums=set(nums)
        result=[]
        for i in range (1,len(nums)+1):
            if i not in new_nums:
                result.append(i)
        return result

        

