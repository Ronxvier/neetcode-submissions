class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        nmap = {}
        for char in s:
            if char in nmap:
                nmap[char] += 1
            else:
                nmap[char] = 1
        for char in t:
            if char in nmap:
                nmap[char] -=1
            else:
                return False
        for key in nmap:
            if nmap[key] != 0:
                return False
        return True
        