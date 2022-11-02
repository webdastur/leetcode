# Author: Abdulaminkhon Khaydarov
# Date: 02/11/22 
# Problem URL: https://leetcode.com/problems/concatenation-of-array/

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums.append(nums[i])
        return nums


if __name__ == '__main__':
    solution = Solution()

    # Example 1
    print(solution.getConcatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1])

    # Example 2
    print(solution.getConcatenation([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1])
