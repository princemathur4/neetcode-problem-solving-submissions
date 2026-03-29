class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {num: i for i, num in enumerate(nums)}
        for i in range(len(nums)):
            target_j = target - nums[i]
            j = d.get(target_j)
            if j is None:
                continue
            if i == j:
                continue
            if nums[i] + nums[j] == target:
                return sorted([i,j])
        
            