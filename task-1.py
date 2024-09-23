class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        prev = 0

        for c in reversed(s):
            value = roman_numerals[c]

            if value < prev:
                result -= value
            else:
                result += value

            prev = value

        return result
