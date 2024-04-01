class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total, prev_value = 0, 0

        for symbol in s:
            value = roman_to_int[symbol]
            total += value

            if prev_value < value:
                total -= 2*prev_value

            prev_value = value

        return total
