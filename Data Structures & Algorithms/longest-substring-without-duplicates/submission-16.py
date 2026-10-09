class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        maxsub = 0
        l = 0
        r = 0
        while r<(len(s)):
            char = s[r]
            if char not in hashset:
                hashset.add(char)
                r+=1
            else:
                while s[l] != char:
                    hashset.remove(s[l])
                    l+=1
                l+=1
                r+=1
            maxsub = max(maxsub, r-l)
        return maxsub