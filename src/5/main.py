testcases = [
    ("babad", "bab"),
    ("cbbd", "bb"),
    ("a", "a"),
    ("ac", "a"),
    ("xabax", "xabax"),
    ("xabay", "aba"),
    ("xabayz", "aba"),
    ("xabayzq", "aba"),
    ("tacocat", "tacocat"),
    ("tacocatq", "tacocat"),
    ("atoyota", "atoyota"),
]


def expand_around_center(s: str, left: int, right: int) -> str:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1 : right]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s

        longest = ""

        for i in range(len(s)):
            # odd length
            odd = expand_around_center(s, i, i)
            # even length
            even = expand_around_center(s, i, i + 1)

            if len(odd) > len(longest):
                longest = odd

            if len(even) > len(longest):
                longest = even

        return longest


def main():
    for s, expected in testcases:
        sol = Solution()
        result = sol.longestPalindrome(s)
        print(f"Result: {result}, Expected: {expected}")
        assert result == expected, f"{result} != {expected}"


if __name__ == "__main__":
    main()
