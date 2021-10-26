# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 09:48:37 2021

@author: jakir
"""

# Book: 10.2

# ======
# Selection Sort
# ======

# def selection_sort(L):
#     """
#     Assumes L is a list of elements that can be compared using <.
#     Sorts L in ascending order.

#     """
#     suffix_start = 0
#     while (suffix_start != len(L)):
        
#         for i in range(suffix_start, len(L)):
#             if L[i] < L[suffix_start]:
#                 L[i], L[suffix_start] = L[suffix_start], L[i]
#         suffix_start += 1
    
#     return L


# L = [3, 8, 1, 0, 11, 2, 4]
# print("Selection sort:", selection_sort(L))


# =====
# Merge sort
# =====

# def merge(left, right):
#     """
#     Assumes left and right are sorted lists.
#     Returns a sorted list containing the elements of left and right.

#     """
#     i, j = 0, 0
#     result = []
    
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
    
#     while i < len(left):
#         result.append(left[i])
#         i += 1
        
#     while j < len(right):
#         result.append(right[j])
#         j += 1
    
#     return result


# def merge_sort(L):
#     """
#     Assumes L is a list.
#     Returns a sorted list with the same element as L.
#     """
#     if len(L) < 2:
#         return L[:]
    
#     middle = len(L)//2
#     left = merge_sort(L[:middle])
#     right = merge_sort(L[middle:])
    
#     return merge(left, right)


# testList = [1,3,5,7,2,6,25,18,13]
# print(merge_sort(testList))









