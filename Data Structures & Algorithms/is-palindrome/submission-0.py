class Solution:
    def isPalindrome(self, s: str) -> bool:
        c= ' '.join(c.lower() for c in s if c.isalnum())

        return c == c[::-1]