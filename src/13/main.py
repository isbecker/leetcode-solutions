testcases = [("III", 3), ("LVIII", 58), ("MCMXCIV", 1994)]


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1,
        }
        arabic = 0
        while len(s) > 0:
            if s[:2] in roman_numerals:
                symbol = s[:2]
                value = roman_numerals[symbol]
                arabic += value
                s = s[2:]
            elif s[:1] in roman_numerals:
                symbol = s[:1]
                value = roman_numerals[symbol]
                arabic += value
                s = s[1:]

        return arabic


def main():
    sol = Solution()
    for case, expected in testcases:
        result = sol.romanToInt(case)
        print(f"Case: {case}, Expected: {expected}, Result: {result}")

        assert result == expected

    print("PASSED")


if __name__ == "__main__":
    main()
