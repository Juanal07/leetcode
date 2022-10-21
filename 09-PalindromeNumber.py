class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        half = int(len(x) / 2)
        for i in range(0, half):
            if x[i] != x[len(x) - i - 1]:
                return False
        return True
