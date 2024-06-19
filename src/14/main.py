from typing import List

testcases = [(["flower", "flow", "flight"], "fl"), (["dog", "racecar", "car"], ""), (["flower", "flowers", "flowering"], "flower")]


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: 

      same_letter = True
      cur = 0
      prefix = ""
      while same_letter:
        try:
          cur_chars = [s[cur] for s in strs]
        except IndexError:
          break
        same_letter = all(char == cur_chars[0] for char in cur_chars)
        if same_letter:
          prefix += cur_chars[0]
        cur += 1
      return prefix


def main():
    sol = Solution()
    for case, expected in testcases:
        result = sol.longestCommonPrefix(case)
        print(f"Case: {case}, Expected: {expected}, Result: {result}")

        assert result == expected

    print("PASSED")


if __name__ == "__main__":
    main()
