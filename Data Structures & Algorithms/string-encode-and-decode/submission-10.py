class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''

        for string in strs:
            encoded += f"{len(string)}#{string}"
        
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            length = ''
            while s[i] != "#":
                length += s[i]
                i += 1
            i += 1
            res.append(s[i : i + int(length)])
            i += int(length)
        
        return res