"""EXAMPLE — what a filled predictions.py looks like (Ch 6 style).

This folder is a reference, not a workspace. Delete it once you've
internalized the pattern, or keep it as a reminder.
"""

# ------------------------------------------------------------
# Puzzle 1
# ------------------------------------------------------------
# PREDICT: [1, 2, 3] then [1, 2, 3]  (I think b gets a copy)
# ACTUAL:  [1, 2, 3] then [1, 2, 3, 4] -- wait, BOTH printed [1,2,3,4]
# VERDICT: WRONG — b = a shares the SAME list object. No copy happens.
#          --> copied to notes/ch06.md "Code that surprised me"
#          --> added one line to traps.md: "b = a never copies"

print("--- puzzle 1 ---")
a = [1, 2, 3]
b = a
b.append(4)
print(a)
print(b)


# ------------------------------------------------------------
# Puzzle 2
# ------------------------------------------------------------
# PREDICT: a unchanged [1, 2, 3], c is [1, 2, 3, 99] (slice copies)
# ACTUAL:  exactly as predicted
# VERDICT: right — a[:] makes a new (shallow) list

print("--- puzzle 2 ---")
a = [1, 2, 3]
c = a[:]
c.append(99)
print(a)
print(c)
