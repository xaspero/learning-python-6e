# exercises/ — Practice Code, One Folder Per Chapter

This folder holds all hands-on practice from the daily loop (Items 2–3 of
the study method: type every example, break it on purpose, predict before
running).

## Structure

```
exercises/
  README.md          (this file)
  _template/         (never edit these — always copy)
    practice.py
    predictions.py
    experiments.py
  ch01/
  ch02/
  ...
```

## Starting a new chapter

From the repo root, one command:

```bash
cp -r exercises/_template exercises/ch06
```

(Replace `ch06` with the chapter number, zero-padded: ch01 ... ch41.)

Then work inside `exercises/ch06/` for the whole chapter. Run any file with:

```bash
python3 exercises/ch06/practice.py
```

## Which file is for what

| File             | Purpose                                                        | When |
|------------------|----------------------------------------------------------------|------|
| `practice.py`    | Book examples you type in, section by section                  | While reading (Item 3) |
| `predictions.py` | Predict-then-run: write expected output BEFORE running         | While reading, whenever you "break it on purpose" |
| `experiments.py` | Your own questions: "what happens if...?"                      | Anytime curiosity strikes |

## Rules

1. **Never edit `_template/` itself.** It stays clean so every chapter
   starts from the same blank slate. If you improve the template, do it
   deliberately and commit it with a message saying so.
2. **Type, never paste.** The templates have empty sections on purpose.
3. **REPL vs file:** quick one-liners (< 5 lines) go in the REPL and are
   throwaway. Anything worth keeping or longer goes in these files.
4. **Wrong predictions are the treasure.** When `predictions.py` proves
   you wrong, that snippet graduates to the chapter note under
   "Code that surprised me" — and possibly to `traps.md`.
5. **Commit the folder with the chapter's note** in the same daily commit.
