# -*- coding: utf-8 -*-

# Exercise 9
# two functions are required:
#   1st: write a file with 100 math exercises combining positive and negative
#   random numbers
#   2nd: must solve every math exercises already created

import random
import re


def create_math_problems(f):
    for i in range(1, 101):
        a = random.randint(-40, 40)
        b = random.randint(-40, 40)
        c = random.randint(-40, 40)
        d = random.randint(-40, 40)
        op_1 = random.choice(['-', '+'])
        op_2 = random.choice(['-', '+'])
        op_3 = random.choice(['-', '+'])

        f.write(
            f'[{i:-3}] {a:-3} {op_1} ( {b:-3}) {op_2} ( {c:-3}) {op_3} '
            f'( {d:-3}) = ______\n'
        )


def solve_math_problems(f):
    math_problems = f.readlines()
    for problem in math_problems:

        pattern = re.compile(r"(-?\d+|\-|\+)")
        match = pattern.findall(problem)
        match.pop(0)
        # print(match)
        cadena = ''
        for i in match:
            cadena += i
        # print(cadena)
        # print(eval(cadena))
        pattern_sb = re.compile(r"(\_+)")
        match_sub = pattern_sb.sub(str(eval(cadena)), problem)
        print(match_sub, end='')


if __name__ == "__main__":
    with open('test-problems.txt', 'w') as f:
        create_math_problems(f)
    with open('test-problems.txt', 'r') as f2:
        solve_math_problems(f2)
    print('hello')
