testcases = [
    (121, True),
    (-121, False),
    (10, False),
]


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = f"{x}"
        backwards = "".join(reversed(s))
        return s == backwards


def main():
    for case, expected in testcases:
        sol = Solution()
        result = sol.isPalindrome(case)

        print(f"Result: {result}, Expected: {expected}")
        assert result == expected

    print("PASSED")


if __name__ == "__main__":
    main()
