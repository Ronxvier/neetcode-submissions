class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxlen = 0
        r,l = 0,0
        while r<len(s):
            windowlen = r-l+1
            count[s[r]] = count.get(s[r],0)+1
            maxfreq = max(count.values())
            valid = (windowlen-maxfreq)<=k
            if not valid:
                count[s[l]]-=1
                l+=1
                windowlen = r-l
            maxlen = max(maxlen,windowlen)
            r+=1
        return maxlen
