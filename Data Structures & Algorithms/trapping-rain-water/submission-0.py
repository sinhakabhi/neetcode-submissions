class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        pref = [0] * n
        suff = [0] * n
        pref[0] = height[0]
        suff[n-1] = height[n-1]

        for i in range(1, n):
            pref[i] = max(pref[i-1], height[i])
        
        for i in range(n-2, -1, -1):
            suff[i] = max(suff[i+1], height[i])
        cnt = 0
        for i in range(0, n):
            cnt += min(pref[i], suff[i])-height[i]
        
        return cnt
