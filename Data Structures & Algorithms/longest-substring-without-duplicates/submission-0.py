class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        max_length = 0
        idx = 0
        for i in range(0,len(s)):
            if s[i] in st:
                while(s[i] in st):
                    st.remove(s[idx])
                    idx+=1
            st.add(s[i])
            max_length = max(max_length, len(st))
        
        return max_length