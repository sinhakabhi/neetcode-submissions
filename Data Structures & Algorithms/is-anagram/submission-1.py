class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        char_s = list(s)
        char_t = list(t)
        char_s.sort()
        char_t.sort()

        for i in range(0, len(char_s)):
            if char_s[i]!=char_t[i]:
                return False
        
        return True