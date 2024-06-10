# leetcode-solutions

This repository contains my solutions to various problems on LeetCode. I will be updating this repository as I solve more problems.

## Tech components

- Python
- [nix](https://nixos.org/)
  - [flake-parts](https://flake.parts)
  - [devenv](https://devenv.sh/)
- [direnv](https://direnv.net/)
- [just](https://github.com/casey/just)
- [rye](https://github.com/astral-sh/rye)

## Problems

| # | Title | Solution | Difficulty |
|---| ----- | -------- | ---------- |
|5|[Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)|[Python](./src/5/main.py)|Medium|
|6|[Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion/)|[Python](./src/6/main.py)|Medium|
|7|[Reverse Integer](https://leetcode.com/problems/reverse-integer/)|[Python](./src/7/main.py)|Medium|

## Running the code

This project is built with [nix](https://nixos.org/). To run the code, you need to have nix installed on your system. Once you have nix installed, you can run the following command to run the code:

```bash
nix develop --impure --command just run <problem_number>
```

`nix develop` will use `devenv` to create a nix-based development environment with all the necessary dependencies. 

For example, to run problem 5, you can run the following command:

```bash
nix develop --impure --command just run 5
```

Technically you can also run the solutions with only Python, as there's nothing in the solutions  that uses any pip packages or anything. But I like to use nix for all my projects, so I'm using it here as well. The locked dependencies using devenv + nix + rye will ensure that the code runs in a reproducible environment (even in the future!).
