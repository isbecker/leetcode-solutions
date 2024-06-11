testcases = [
    ("42", 42),
    ("   -042", -42),
    ("1337c0d3", 1337),
    ("0-1", 0),
    ("words and 987", 0),
    ("-91283472332", -2147483648),
    ("+1", 1),
    ("21474836460", 2147483647),
]


class Solution:
    def myAtoi(self, s: str) -> int:
        positive = True
        number = 0
        digits = 0
        current = ""
        zero = ord("0")
        nine = ord("9")

        for i, c in enumerate(s.lstrip()):
            c_ord = ord(c)
            if i == 0:
                if c == "-":
                    positive = False
                    continue
                elif c == "+":
                    positive = True
                    continue
            if c_ord >= zero and c_ord <= nine:
                digits += 1
                current += c
            else:
                break

        for i, c in enumerate(current):
            numeric_value = ord(c) - zero
            number += 10 ** (digits - i - 1) * numeric_value
        return min(number, (2**31) - 1) if positive else (min(number, (2**31)) * -1)


def main():
    for case, expected in testcases:
        sol = Solution()
        result = sol.myAtoi(case)

        print(f"Result: {result}, Expected: {expected}")
        assert result == expected

    print("PASSED")


if __name__ == "__main__":
    main()
