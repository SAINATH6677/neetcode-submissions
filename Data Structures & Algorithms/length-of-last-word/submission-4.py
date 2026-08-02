class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i=len(s)-1;
        count = 0

        while(i>=0):
            if not s[i].isalpha() and count > 0:
                break
            if(s[i].isalpha()):
                count+=1
            i-=1
                

        return count

        