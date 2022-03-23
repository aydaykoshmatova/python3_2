
"""
Attribute 1 = list: given array ( 3 >= len(array) <= 10_000)
Attribute 2 = sum: 16

example:
    Input: [2, 3, 4, 5, 6, 7, 8, 9], 16
    Output: [5, 7]
"""

class Solution:

    def two_sum(self, array: list, sum: int) -> list:
        for i in range(len(array)):
            for j in range(i, len(array)):
                if array[i] + array[j] == sum:
                    return [i, j]






