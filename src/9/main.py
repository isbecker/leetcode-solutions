testcases = [(121, True), (-121, False), (10, False), (2**31, False), (0, True), (1, True), (1000001, True), (10021, False)]


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:  # all negative numbers will be non-palendromic
            return False
        exponent = 12
        digits = []
        while exponent >= 0:
            power_of_ten = 10**exponent
            mod_power = 10 ** (exponent + 1)
            digit = x % mod_power // power_of_ten
            exponent -= 1

            digits.append(digit)

        nonzero_digit_encountered = False
        exponent = 0

        reversed_num = 0
        for d in digits:
            if not nonzero_digit_encountered and d == 0:
                continue
            else:
                nonzero_digit_encountered = True
            reversed_num += 10**(exponent) * d
            exponent += 1

        return reversed_num == x

def main():
    for case, expected in testcases:
        sol = Solution()
        result = sol.isPalindrome(case)

        print(f"Result: {result}, Expected: {expected}")
        assert result == expected

    print("PASSED")


if __name__ == "__main__":
    main()
