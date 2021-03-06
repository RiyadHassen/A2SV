# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 18:38:09 2021

@author: riyad
"""

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        minimum = -float('inf')
        index = 0
        for i in range(len(nums)):
            if nums[i] >= minimum:
                minimum = nums[i]
            else:
                index = i
                break
        l = nums[0:index]
        left = self.binarySearch(l,target)
        if left:
            return left
        r=nums[index:]
        right = self.binarySearch(r,target)
        if right:
            return right
    def binarySearch(self,nums,target):
        start = 0
        end = len(nums)-1
        while start <= end:
            middle = start + (end-start)//2
            if nums[middle]==target:
                return True
            if nums[middle] > target:
                end = middle -1
            elif nums[middle] < target:
                start = middle + 1
        return False