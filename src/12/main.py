testcases = [(3749, "MMMDCCXLIX"), (58, "LVIII"), (1994, "MCMXCIV")]


class Solution:
    def intToRoman(self, num: int) -> str:
        roman_numerals = [
            ("M", 1000),
            ("CM", 900),
            ("D", 500),
            ("CD", 400),
            ("C", 100),
            ("XC", 90),
            ("L", 50),
            ("XL", 40),
            ("X", 10),
            ("IX", 9),
            ("V", 5),
            ("IV", 4),
            ("I", 1)
        ]
        
        roman = ""
        
        for symbol, value in roman_numerals:
            count = num // value
            roman += symbol * count
            num -= value * count
        
        return roman



def main():
    sol = Solution()
    for case, expected in testcases:
        result = sol.intToRoman(case)
        assert result == expected

        print(f"Expected: {expected}, Result: {result}")

    print("PASSED")


if __name__ == "__main__":
    main()
