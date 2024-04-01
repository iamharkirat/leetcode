from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = min(len(s) for s in strs)
        prefix = ""

        for i in range(min_length):
            char = strs[0][i]
            for s in strs:
                if s[i] != char:
                    return prefix

            prefix += char

        return prefix
