class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for N in nums:
            if N in hashset:
                return True
            hashset.add(N)
        return False        
                
