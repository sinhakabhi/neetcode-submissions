class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = "".join(char for char in s if char.isalnum()).lower()
        p1 = 0
        p2 = len(str)-1
        while(p1<=p2):
            if str[p1]!=str[p2]:
                return False
            p1=p1+1
            p2=p2-1
        return True
