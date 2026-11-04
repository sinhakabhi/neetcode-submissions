class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        p1 = 0
        p2 = n-1
        max_area = -1

        while p1<=p2:
            min_elem = min(height[p1], height[p2])
            max_area = max(max_area, min_elem*(p2-p1))
            if min_elem==height[p1]:
                p1+=1
            else:
                p2-=1

        return max_area