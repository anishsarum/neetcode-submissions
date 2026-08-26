class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''

        for string in strs:
            encoded += str(len(string)) + "#" + string
        
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        l = r = 0

        while l < len(s) and r < len(s):
            length = ''
            while s[r] != "#":
                length += s[r]
                r += 1
            r += 1
            res.append(s[r : r + int(length)])
            r += int(length)
            l = r
        
        print(res)
        
        return res