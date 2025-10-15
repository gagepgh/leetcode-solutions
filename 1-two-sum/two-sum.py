def solve(self, nums, target):
    hashMap = {};
    for x in range(len(nums)):
        num = nums[x];
        if target-num in hashMap:
            return [hashMap.get(target-num),x];
        hashMap[num] = x;
    return []

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return solve(self,nums,target);