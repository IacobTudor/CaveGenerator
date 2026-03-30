# Cave Generator

This project generates cave-like structures using **cellular automata**.  
It allows you to visualize a 2D cave grid where walls and empty spaces form natural-looking cave patterns.

---

## Features

- Generate caves on an **NxN grid**.
- Adjust **wall density** with a parameter (1-100).
- Simple **cellular automata rules** for realistic cave shapes:
  - A cell becomes empty if it has ≤2 wall neighbors.
  - A cell becomes wall if it has ≥6 wall neighbors.
  - Otherwise, it stays the same.
- Output visualized with **matplotlib**.
- Fully customizable colors for walls and empty spaces.

---

## Example Output

![Example cave](cave.png)

---

## Requirements

- Python 3.x
- matplotlib

Install matplotlib if you don’t have it:

```bash
pip install matplotlib
