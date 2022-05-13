class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            a = str(x)
            b = a[::-1]
            if a == b:
                return True
