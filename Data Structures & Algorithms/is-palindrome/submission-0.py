class Solution:
    def isPalindrome(self, s: str) -> bool:
        simplified = "".join(c.lower() for c in s if c.isalnum())
        
        return simplified == simplified[::-1]