class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        str_len = len(x_str)
        idx_range = str_len // 2

        for i in range(idx_range):
            if x_str[i] != x_str[str_len-i-1]:
                return False
        return True
