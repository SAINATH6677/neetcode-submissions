class Solution:
    def scoreOfString(self, s: str) -> int:
        i = 1
        ans = 0
        while(i<len(s)):
            ans = ans + abs(ord(s[i]) - ord(s[i-1]))
            i+=1

        return ans
