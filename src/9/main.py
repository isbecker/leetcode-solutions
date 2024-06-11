testcases = [(121, True), (-121, False), (10, False), (2**31, False), (0, True), (1, True), (1000001, True), (10021, False)]


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        original = x
        reversed_num = 0
        
        while x != 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x = x // 10
        
        return original == reversed_num


def main():
    for case, expected in testcases:
        sol = Solution()
        result = sol.isPalindrome(case)

        print(f"Result: {result}, Expected: {expected}")
        assert result == expected

    print("PASSED")


if __name__ == "__main__":
    main()
