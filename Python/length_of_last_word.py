"""
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.


Example 1:
----------

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
----------

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
----------

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 
-------------
Constraints: |
-------------

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.

NOTE: we are purposely not using any python built in functions to this one, defeats the purpose of the exercise. 
"""



class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        #set a pointer to the end of the string, By iterating backward we can always ensure to never have to read more than we need to
        p = len(s) - 1
        c = 0 
       
        while p >= 0:
            #if it is a space but the number of charcters seen is 0, then just move down the line until we find the first chracter
            if s[p] == " " and c == 0 :
                p -= 1
            #if it is a character, then move to next position and increment the last word char counter
            elif s[p] != " ":
                c += 1
                p-= 1
            #last case is that is is a space following the word, which we know because the valid characters seen is greater than 0
            else:
                return c
              
        #base case of no word in the string
        return c
