
"""
461. Hamming Distance
Solved
Easy
Topics
Companies
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

 

Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
Example 2:

Input: x = 3, y = 1
Output: 1
"""

class Solution(object):
    def hammingDistance(self,x, y):
        bin_x=bin(x)[2:]
        bin_y=bin(y)[2:]
        list_x=list(bin_x)
        list_y=list(bin_y)
        count=0
        while len(list_x)!=len(list_y):
            if len(list_x)<len(list_y):
                list_x.insert(0,'0')
            else:
                list_y.insert(0,'0')
        for i in range(len(list_x)):
            if list_x[i]!=list_y[i]:
                count+=1
        return count