from basicCalculator2 import calculate


"""
https://leetcode.com/problems/basic-calculator/

Example:
"(1+(4+ 15+2)-3)+(6+8)" -> 33
" 2-1 + 2 " -> 3
"""

class Solution:
    def calculate(self, s):
        num = 0
        stack = [1]; result = 0; prev_sign = 1
        sign_map = {'+':1 , '-':-1}

        for i in range(len(s)):
            letter = s[i]
            if letter.isdigit():
                num = num * 10 + int(letter)
            elif letter in ['+', '-']:
                result += prev_sign * num
                num = 0
                prev_sign= sign_map[letter] * stack[-1]
            elif letter == '(':
                stack.append(prev_sign)
            elif letter == ')':
                stack.pop(-1)

        result += prev_sign * num
        return result

    def calculate(self, a, b):
        pass

    def calculate_with_mult_div(self, s):
        num = 0
        stack = [1]; result = 1; prev_sign = 1
        sign_map = {'+':1 , '-':-1}

        for i in range(len(s)):
            letter = s[i]
            print(letter, num, prev_sign, result)
            if letter.isdigit():
                num = num * 10 + int(letter)
            elif letter in ['+', '-']:
                result += prev_sign * num
                num = 0
                prev_sign= sign_map[letter] * stack[-1]
            elif letter in ['*', '/']:
                result *= prev_sign * num
                num = 0
                prev_sign= stack[-1]
            elif letter == '(':
                stack.append(prev_sign)
            elif letter == ')':
                stack.pop(-1)

        result += prev_sign * num
        return result


2 * 62 / 3
3+2*2
print(Solution().calculate_with_mult_div("2 * 62 / 3"))



# print(Solution().calculate("(1+(4+15+2)-3)+(6+8)"))


s = "(1+(4+ 156+2)-3)+(6-284+8)" # 110
# q = list(s.replace(' ', ''))
# print(Solution().calculate(s))
# print(Solution().calculate("-3 + 8"))


# s = "12 + 15 / 16" # 110
# q = list(s.replace(' ', ''))
# print(Solution().calculate(list(s)))