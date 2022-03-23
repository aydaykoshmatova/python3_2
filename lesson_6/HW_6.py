def get_list() -> list:
    return list(range(0, 1_000_000_000, 2))

class Solution:

    def find_target(self, list, target):
        for i in range(target):
            left, right = 0, len(list) - 1

            while left <= right:

                middle = (left + right) // 2

                if list[middle] == target:
                    return middle

                if list[middle] < target:
                    left = middle + 1

                elif list[middle] > target:
                    right = middle - 1
