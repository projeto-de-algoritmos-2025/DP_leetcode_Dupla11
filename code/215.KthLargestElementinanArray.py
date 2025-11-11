import math
import bisect
import random
from typing import List
import sys


class Solution:

    def quickSelect(self, nums: List[int], k: int, l: int, r: int):
        # implementação iterativa com pivot aleatório e partição 3-way
        if l == r:
            return nums[l]

        pivot_idx = random.randint(l, r)
        pivot = nums[pivot_idx]
        nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]

        # partição 3-way para lidar com valores iguais
        # intervalo menor é [l, lt-1]
        # intervalo maior é [gt+1, r]
        # intervalo igual é [lt, gt]
        lt, i, gt = l, l, r
        while i <= gt:
            if nums[i] < pivot:
                nums[lt], nums[i] = nums[i], nums[lt]
                lt += 1
                i += 1
            elif nums[i] > pivot:
                nums[i], nums[gt] = nums[gt], nums[i]
                gt -= 1
            else:
                i += 1

        # intervalo igual é [lt, gt]
        if k < lt:
            return self.quickSelect(nums, k, l, lt - 1)
        elif k > gt:
            return self.quickSelect(nums, k, gt + 1, r)
        else:
            return nums[k]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        return self.quickSelect(nums, k, 0, len(nums)-1)
