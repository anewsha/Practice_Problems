class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def bs(nums, target, left, right):
            if left>right:
                return -1
            m = (left+right)//2
            if nums[m]==target:
                return m
            if nums[m]<target:
                return (bs(nums,target,m+1, right))
            else:
                return (bs(nums, target,0,m-1))
        
        return bs(nums,target,0,len(nums)-1)
solution = Solution()
print(solution.search([-1,0,3,5,9,12],9))
