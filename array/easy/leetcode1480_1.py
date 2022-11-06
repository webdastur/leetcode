# Author: Abdulaminkhon Khaydarov
# Date: 06/11/22 
# Problem URL: https://leetcode.com/problems/running-sum-of-1d-array/

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
        return nums


if __name__ == '__main__':
    solution = Solution()

    # Example 1
    print(solution.runningSum([1, 2, 3, 4]) == [1, 3, 6, 10])

    # Example 2
    print(solution.runningSum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5])

    # Example 3
    print(solution.runningSum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17])
