# Author: Abdulaminkhon Khaydarov
# Date: 30/10/22 
# Problem URL: https://leetcode.com/problems/build-array-from-permutation/

from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # "nums" ni uzunligi bilan teng "ans" listini yaratib olamiz
        ans: List[int] = [0 for _ in nums]

        # "0" dan "nums" uzunligigacha sikl yaratib "ans[i]" ni "nums[nums[i]]" ga tenglab chiqamiz.
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]

        return ans


if __name__ == '__main__':
    solution = Solution()

    # Example 1
    print(solution.buildArray([0, 2, 1, 5, 3, 4]) == [0, 1, 2, 4, 5, 3])

    # Example 2
    print(solution.buildArray([5, 0, 1, 2, 3, 4]) == [4, 5, 0, 1, 2, 3])
