"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.



Example 1:
----------

Input: digits = [1,2,3]
Output: [1,2,4]

Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
----------

Input: digits = [4,3,2,1]
Output: [4,3,2,2]

Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
----------

Input: digits = [9]
Output: [1,0]

Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #set the carry to 1 since we know we are addng one
        carry = 1
        
        #iterate through list backwards
        for i in range(len(digits) - 1, -1, -1):
            #calculate waht the digit would be if we added 1 to it
            num = digits[i] + 1
            
            #if it is less than 10, add one to the index digit and retur the list
            if num < 10:
                digits[i] = digits[i] + carry
                return digits
            #otherwise set the digit to 0 and move to the next digit
            else:
                digits[i] = 0
        
        #if we get to the end of the list, we need to append a 1, to the beginning of the list adn return it
        digits.insert(0,carry)
        return digits
    
