''' Question:- LeetCode #167 – Two Sum II (Input Array Is Sorted)'''

class Solution:
    def twoSum(self, numbers, target):
        
        left = 0
        right = len(numbers) - 1

        while left < right:
            s = numbers[left] + numbers[right]

            if s == target:
                return [left + 1, right + 1]
            elif s < target:
                left += 1
            else:
                right -= 1



if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9

    sol = Solution()
    result = sol.twoSum(numbers, target)
    print("Output:", result)
