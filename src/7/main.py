testcases = [
    (123, 321),
    (-123, -321),
    (120, 21),
    (0, 0),
    (1534236469, 0),
    (-2147483648, 0)
]

class Solution:
    def reverse(self, x: int) -> int:
      positive = x > 0

      if not positive:
        x *= -1
      s = int(f"{x}"[::-1], base=10)

      if not positive:
        s *= -1
      return s if s < 2 ** 31 - 1 and s > -2**31 else 0 

def main():
  for x, expected in testcases:
    result = Solution().reverse(x)
    print(f"result={result}, expected={expected}")
    assert result == expected, f"{result} != {expected}"
  print("PASSED")


if __name__ == "__main__":
    main()
