"""Chapter 03 — Predictions

The predict-then-run drill. THE ONE RULE: fill in PREDICT before you run.
Running first and writing the "prediction" after is lying to yourself and
teaches nothing.

Workflow per puzzle:
  1. Write a small snippet (from the book, modified — or your own).
  2. Write your PREDICT comment: exact expected output, or "error: <why>".
  3. Run:  python3 predictions.py
  4. Fill ACTUAL. If PREDICT != ACTUAL → mark it WRONG and copy the
     puzzle into the chapter note under "Code that surprised me".

Keep every puzzle, right or wrong. Re-running this file cold weeks later
is a free self-quiz.
"""

# ------------------------------------------------------------
# Puzzle 1
# ------------------------------------------------------------
# PREDICT: I want to raise the content of x to the power of 8
# ACTUAL: TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
# VERDICT: WRONG

import sys
import sys

print("--- puzzle 1 ---")
# (code here)

print(sys.platform)
print(2 ** 100)
x = 'Hack!'

print(x ** 8)  # repeat the string x 8 times


# ------------------------------------------------------------
# Puzzle 2
# ------------------------------------------------------------
# PREDICT:
# ACTUAL:
# VERDICT:

print("--- puzzle 2 ---")
# (code here)


# ------------------------------------------------------------
# Puzzle 3
# ------------------------------------------------------------
# PREDICT:
# ACTUAL:
# VERDICT:

print("--- puzzle 3 ---")
# (code here)


# (add as many as the chapter deserves — mutation/scope/iteration
#  chapters earn 8-10 puzzles; light chapters may earn 3)
