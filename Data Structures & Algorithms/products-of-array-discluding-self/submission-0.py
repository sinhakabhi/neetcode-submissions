class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = []
        # for i in range(0,len(nums)):
        #     prod=1
        #     for j in range(0, len(nums)):
        #         if i==j:
        #             continue
        #         prod *= nums[j]
        #     res.append(prod)
        
        # return res
        res = []
        pref = [1 for i in range(len(nums))]
        suff = [1 for i in range(len(nums))]

        for i in range(1, len(nums)):
            pref[i] = pref[i-1]*nums[i-1]
        
        for i in range(len(nums)-2, -1,-1):
            suff[i] = suff[i+1]*nums[i+1]

        for i in range(len(nums)):
            prod = pref[i]*suff[i]
            res.append(prod)
        return res