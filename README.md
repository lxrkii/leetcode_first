<h1 align="center">How to solve<a href="https://daniilshat.ru/" target="_blank"></a> 
<img src="https://i.imgur.com/VFa4Mjqr.jpg" height="32" weight="32"/></h1>

Link on problem: https://leetcode.com/problems/regular-expression-matching/

1. `dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]`:
   - This line initializes a 2D array `dp` (Dynamic Programming matrix) with dimensions `(len(s) + 1) x (len(p) + 1)`. It is used to store intermediate results for dynamic programming.

2. `dp[0][0] = True`:
   - It sets the value at the top-left corner of the DP matrix to `True`. This is because an empty pattern (`p`) matches an empty string (`s`).

3. `for j in range(1, len(p) + 1):`:
   - This loop iterates through the characters in the pattern `p`, starting from the second character (index 1) to the end.

4. `if p[j - 1] == '*':`:
   - It checks if the current character in `p` is an asterisk '*'.

5. `dp[0][j] = dp[0][j - 2]`:
   - If the current character in `p` is '*', it sets the value in the DP matrix at the first row and `j`-th column to the value two columns to the left. This is because '*' can match zero of the preceding element.

6. Nested Loop:
   - The code enters a nested loop that iterates through the characters in both the string `s` and the pattern `p`.

7. `if p[j - 1] == s[i - 1] or p[j - 1] == '.':`:
   - It checks if the current characters in `p` and `s` match or if the current character in `p` is a period ('.'). In either case, it means we have a potential match.

8. `dp[i][j] = dp[i - 1][j - 1]`:
   - If there is a match or the current character in `p` is '.', it sets the value in the DP matrix at row `i` and column `j` to the value diagonally above and to the left. This represents the situation where the current characters match.

9. `elif p[j - 1] == '*':`:
   - If the current character in `p` is '*', it checks two conditions:
      - `dp[i][j - 2]` represents the case where '*' matches zero of the preceding element.
      - `dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.')` represents the case where '*' matches one or more of the preceding element. This involves checking if the preceding characters in `s` and `p` match or if the preceding character in `p` is '.'.

10. Finally, the function returns `dp[len(s)][len(p)]`, which represents whether the entire string `s` matches the entire pattern `p`.

[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Tess+Talk+About+IT)](https://git.io/typing-svg)
