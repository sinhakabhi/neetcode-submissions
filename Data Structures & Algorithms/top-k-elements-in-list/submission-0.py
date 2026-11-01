class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in nums:
            if i in map:
                map[i]+=1
            else:
                map[i]=1
        sorted_map = dict(sorted(map.items(), key=lambda item:item[1], reverse=True))
        res = []
        l=list(sorted_map)
        idx = 0
        while(k>0):
            res.append(l[idx])
            idx+=1
            k-=1
        return res