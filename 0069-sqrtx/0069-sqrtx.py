class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l <= r:
            mid = (l+r)//2
            cal = mid * mid 
            if cal < x:
                l = mid + 1
            elif cal > x:
                r = mid - 1
            else:
                return mid
        else:
            return r
