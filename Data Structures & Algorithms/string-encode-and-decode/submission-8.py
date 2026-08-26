class Solution:
    def encode(self, strs: List[str]) -> str:
        encoding = ""
        for s in strs:
            encoding += f"{len(s)}#{s}"
        return encoding

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            n = ""
            while s[i] != "#":
                n += str(s[i])
                i += 1
            i += 1
            decoded.append(s[i:i+int(n)])
            i += int(n)
        return decoded