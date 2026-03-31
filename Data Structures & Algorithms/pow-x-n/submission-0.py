class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        neg = n < 0
        n = abs(n)

        result = 1.0
        for i in range(n):
            result *= x
        
        if neg:
            return 1 / result
        else:
            return result
