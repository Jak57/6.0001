# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 09:49:08 2021

@author: jakir
"""

### Book

# =============
# 9.3.2: Logarithmic Complexity
# =============

# =========
# ExampLe: Converting int to str
# =========

# def intToStr(i):
#     """
#     Returns string representation of i
#     i (int): non-negative int

#     """
#     digits = "0123456789"
#     if i == 0:
#         return "0"
    
#     result = ""
#     while i > 0:
#         result = digits[i%10] + result
#         i = i//10
#     return result


# def addDigits(n):
#     """
#     Return the sum of digits of n
#     n (int): non-negative integer

#     """
    
#     string_representation = intToStr(n)
#     val= 0
#     for char in string_representation:
#         val += int(char)
        
#     return val

# print(addDigits(12345))


# ========
# 9.3.6: Exponential Complexity
# ========

# Example: Generating power set

# def getBinaryRep(n, numDigits):
#     """
#     Assumes n and numDigits are non-negative ints.
#     Returns a string of length numDigits that is a 
#     binary representation of n

#     """
#     result = ""
#     while n > 0:
#         result = str(n%2) + result
#         n = n//2
    
#     if len(result) > numDigits:
#         raise ValueError("not enough digits")
    
#     for i in range(numDigits - len(result)):
#         result = "0" + result
        
#     return result


# def getPowerset(L):
#     """
#     Assumes L is a list.
#     Returns a list of lists that contains all 
#     possible combinations of elements of L. 

#     """
#     powerset = []
#     for i in range(0, 2**len(L)):
#         binStr = getBinaryRep(i, len(L))
#         subset = []
        
#         for j in range(len(L)):
#             if binStr[j] == "1":
#                 subset.append(L[j])
#         powerset.append(subset)
        
#     return powerset


# L = [1, 2, 3, 4]
# print(getPowerset(L))


# ============
# Slide
# ============

# def bisect_search1(L, e):
#     if L == []:
#         return False
#     elif len(L) == 1:
#         return L[0] == e
#     else:
#         half = len(L)//2
        
#         if L[half] > e:
#             return bisect_search1(L[:half], e)
#         else:
#             return bisect_search1(L[half:], e)

# L = [2, 3, 1, 5, 7, 9]
# print(bisect_search1(L, 50))


# Another approach (Efficient)

def bisect_search2(L, e):
    def bisect_search_helper(L, e, low, high):
        if low == high:
            return L[low] == e
        
        mid = (low + high)//2
        if L[mid] > e:
            if low == mid:
                return False
            return bisect_search_helper(L, e, low, mid-1)
        elif L[mid] == e:
            return True
        else:
            return bisect_search_helper(L, e, mid+1, high)
    
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L)-1)

testList = []
for i in range(1000):
    testList.append(i)

print(bisect_search2(testList, 76))




