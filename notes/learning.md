# Learning notes – Week 1

## Python
- `for r in regions` gives the item itself ("FR"), not its position. Use `regions[i]` only when you need the position.
- `except Exception as e:` then print `e`, so you see *why* it failed.
- `os.makedirs(folder, exist_ok=True)`: without `exist_ok=True`, the 2nd run crashes because the folder already exists.
- Style: `not x` instead of `x == False`, snake_case names, no brackets around `if` conditions, ALL_CAPS only for constants.
- `",".join(list)` glues strings with commas. Numbers need `map(str, list)` first.
- `","` inside `{}` of an f-string only works on Python 3.12+. Use `','` to be safe.
- See a function's parameters: hover / Ctrl+click / docs.python.org. Leading `_` = private.
- Save (Ctrl+S) before running or `git status`. Unsaved changes don't exist for Python or git.

## GitHub Actions
- Exit code 0 = green run, non-zero = red run.
- cron runs in UTC. Fields: minute hour day month weekday. `47 9 * * *` = every day 09:47 UTC. Avoid :00, when the queue is busy and runs start late.
- `workflow_dispatch` = the manual "Run workflow" button.
- `permissions: contents: write` lets the bot push. Without it the push is refused and the run goes red.
- `actions/checkout` copies the repo onto GitHub's empty machine.
- `setup-python` locks the Python version (3.12).
- Commit only if there are changes: `git commit` with nothing to commit exits with 1, so the run goes red.
- The bot pushes to GitHub, not to my PC. My PC gets the files with `git pull`.

## Git
- clone / pull / add / commit / push. Add only the file I changed.
- Always pull first. Push rejected as "behind" → `git pull --rebase`, then push.
- Branch = a separate line of commits.
- Git ignores empty folders.