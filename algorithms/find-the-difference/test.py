#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/find-the-difference/description/
##    ,-----------
##    | Given two strings s and t which consist of only lowercase letters.
##    | 
##    | String t is generated by random shuffling string s and then add one more letter at a random position.
##    | 
##    | Find the letter that was added in t.
##    | 
##    | Example:
##    | 
##    | Input:
##    | s = "abcd"
##    | t = "abcde"
##    | 
##    | Output:
##    | e
##    | 
##    | Explanation:
##    | 'e' is the letter that was added.
##    `-----------
##    
## Basic Idea:
## Complexity:
## Tags:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-23 18:22:06>
##-------------------------------------------------------------------
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
if __name__ == '__main__':
    s = Solution()
    print s.findTheDifference("abcd", "abcde")
    print s.findTheDifference("abcd", "")
    print s.findTheDifference("", "abcde")
## File: test.py ends
