testcases = [
    ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
    ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
    ("A", 1, "A"),
    ("AB", 1, "AB"),
    ("AB", 2, "AB"),
    ("ANOTHEREXAMPLE", 10, "ANOTHEERLEPXMA"),
    ("ONEMOREEXAMPLEFORTESTINGPURPOSES", 5, "OXRPNEAOTGUSEEMFENREMRPESIPSOLTO")
]


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        grid = [[] for _ in range(numRows)]
        s_len = len(s)

        i = 0
        while i < s_len:
            for j in range(numRows):
                if i >= s_len:
                    break
                print(i,j, s[i])
                grid[j].append(s[i])
                i += 1
            for j in range(numRows - 2, 0, -1):
                if i >= s_len:
                    break
                print(i,j, s[i])
                grid[j].append(s[i])
                i += 1

        zigzag = "".join(["".join(row) for row in grid])

        return zigzag


def main():
    for s, numRows, expected in testcases:
        result = Solution().convert(s, numRows)
        print(f"result={result}, expected={expected}")
        assert result == expected, f"{result} != {expected}"
    print("PASSED")


if __name__ == "__main__":
    main()