def get_list() -> list:
    return list(range(0, 1_000_000_000, 2))

class Solution:

    def find_target(self, list, target):




        left, right = 0, len(list) - 1

        while left <= right:

            middle = (left + right) // 2

            if left[middle] == right:
                return middle

            if left[middle] < right:
                left = middle + 1

            elif left[middle] > right:
                right = middle - 1




