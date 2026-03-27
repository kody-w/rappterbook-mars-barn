"""Mars Barn — Colony entry point.

Run the multi-colony simulation for a configurable number of sols.
Default: 1 sol (the minimum proof of life).

Usage:
    python src/main.py          # 1 sol, default config
    python src/main.py 500      # 500 sols
    python src/main.py 500 42   # 500 sols, seed 42
"""
from __future__ import annotations
import sys
from multicolony_v5 import run, show

def main(maxs: int = 1, seed: int = 42) -> dict:
    """Run the colony simulation and display results."""
    result = run(maxs=maxs, seed=seed)
    show(result)
    return result

if __name__ == "__main__":
    maxs = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 42
    main(maxs=maxs, seed=seed)
