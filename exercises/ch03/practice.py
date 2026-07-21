"""Chapter 03 — <How You Run Programs>

Book examples, typed in by hand while reading (study method Item 3).
One section per major heading in the chapter. Run the whole file often:

    python3 practice.py

Every print gets a label so the output reads like a story, not a
mystery wall of values.
"""

# ============================================================
# SECTION: <Program Files>
# Book page: ~34
# ============================================================

# (type the book's example here, then confirm it matches the book's output)

# A first Python script
# script1.py

import sys
print(sys.platform)
print(2 ** 100)
x = 'Hack!'

print(x * 8)  # repeat the string x 8 times

# --- break it on purpose ---
# What I changed: print(x ** 8)
# What I expected: Hack! raised to the power of 8
# What actually happened: TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'


# ============================================================
# SECTION: <second major heading>
# Book page: ~
# ============================================================




# ============================================================
# SECTION: <third major heading>
# Book page: ~
# ============================================================




# ============================================================
# TAKEAWAY (fill at the end of the reading session, from memory,
# 1-3 lines: what did this chapter's code actually teach me?)
# ============================================================
#
#
