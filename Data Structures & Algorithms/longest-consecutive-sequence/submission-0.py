class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for i in nums:
            s.add(i)
        
        longest = 0
        for i in nums:
            curr = i
            prev = curr-1
            if prev not in s:
                cnt = 1
                next = curr+1
                while next in s:
                    cnt = cnt+1
                    next = next+1
                longest = max(longest, cnt)
        
        return longest