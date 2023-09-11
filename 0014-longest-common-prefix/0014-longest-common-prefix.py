class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        stack = strs[0]
        for i in range(1, len(strs)):
            str = strs[i]
            result = ""
            index = 0
            while index<len(stack) and index<len(str):
                if stack[index] == str[index]:
                    result += str[index]
                    index += 1
                else:
                    break
            stack = result
        return stack
                
