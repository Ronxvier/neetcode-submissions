class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mymap={}
        for str in strs:
            key = ''.join(sorted(str))
            if key not in mymap:
                mymap[key] = list({str})
            else:
                mymap[key].append(str)
        return list(mymap.values())