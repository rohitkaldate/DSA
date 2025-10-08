class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = sentence.lower()
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for char in alphabet:
            if char not in s:
                return False
        return True