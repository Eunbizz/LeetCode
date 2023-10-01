class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        prevIndex = self.getRow(rowIndex - 1)
        res = [1]*(len(prevIndex)+1)
        
        for i in range(1,len(res)-1):
            res[i] = prevIndex[i-1]+prevIndex[i]
            
        return res
