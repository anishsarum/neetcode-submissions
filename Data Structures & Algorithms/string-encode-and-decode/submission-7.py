class Solution:
    def __init__(self):
        self.split = "--->--->--->"

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return
        return self.split.join(strs)

    def decode(self, s: str) -> List[str]:
        if not s and isinstance(s, str):
            return [""]
        elif not s:
            return []
        return s.split(self.split)