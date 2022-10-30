# Author: Abdulaminkhon Khaydarov
# Date: 30/10/22 
# Problem URL: https://leetcode.com/problems/build-array-from-permutation/

from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # nums ni uzunligini n ga tenglab olamiz.
        n = len(nums)

        for i in range(len(nums)):
            # "nums[i]" elementini vaqtincha "num" ga olib turamiz
            num = nums[i]

            # "nums[num]" elementini "n" ga bo'lib qoldiqni "b" ga tenglab turamiz.
            b = nums[num] % n

            # "nums[i]" ga "n * b + num" ni tenglab olamiz.
            nums[i] = n * b + num

        for i in range(len(nums)):
            # "nums[i]" ni "nums[i]" ni "n" ga bo'lib butun qismiga tenglab olamiz.
            nums[i] = nums[i] // n

        return nums


if __name__ == '__main__':
    solution = Solution()

    # Example 1
    print(solution.buildArray([0, 2, 1, 5, 3, 4]) == [0, 1, 2, 4, 5, 3])

    # Example 2
    print(solution.buildArray([5, 0, 1, 2, 3, 4]) == [4, 5, 0, 1, 2, 3])
