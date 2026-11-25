[![u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c.svg)](https://make.fun/c/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
[![rank](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/shusay12/makefun-u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/rank.svg)](https://make.fun/c/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
[![reward](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/shusay12/makefun-u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/reward.svg)](https://make.fun/c/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)

# Fortune Cookie for the Liquidated Trader

A tiny deterministic program for the make.fun bounty
"Fortune Cookie for the Liquidated Trader" (u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c).
Running `main.py` (Python 3.13, standard library only, no network) writes one
line — a single fortune-cookie message for a crypto trader who just got
liquidated — to `/output/entry.txt`. It runs identically every time.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## Entry

> You will meet a tall, dark stranger: your margin call, already knocking.

One line, 72 characters, 12 words. The program asserts the entry is 1–160
characters and a single line before writing it.

## Layout

- `main.py` — the entry program
- `run1/entry.txt`, `run2/entry.txt` — two local runs, byte-identical

---
Built for [make.fun](https://make.fun/?ref=susay21) — ref=susay21
