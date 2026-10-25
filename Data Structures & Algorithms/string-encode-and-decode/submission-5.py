class Solution:
    empty = False

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: self.empty = True
        return "#/".join(strs)
    def decode(self, s: str) -> List[str]:
        if len(s) == 0 and self.empty: return []
        return s.split("#/")