''' Question:- LeetCode #26 – Remove Duplicates from Sorted Array'''

class Solution:
    def removeDuplicates(self, nums):
        
        if len(nums) == 0:
            return 0

        i = 0   # pointer for unique elements

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1



if __name__ == "__main__":
    
    nums = [0,0,1,1,1,2,2,3,3,4]
    
    sol = Solution()
    k = sol.removeDuplicates(nums)

    print("Number of unique elements:", k)
    print("Updated array:", nums[:k])
