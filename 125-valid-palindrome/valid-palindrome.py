class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = "".join(ch.lower() for ch in s if ch.isalnum())
        return res == res[::-1]
        # if res==res1:
        #     return True
        # else:
        #     return False

