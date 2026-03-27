"""Breathing test — prove the colony runs for 1 sol without crashing."""
from __future__ import annotations
import subprocess
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "src"

def test_colony_breathes_1sol():
    """Run src/main.py for 1 sol and assert clean exit."""
    result = subprocess.run(
        [sys.executable, str(SRC / "main.py")],
        capture_output=True, text=True, timeout=30
    )
    assert result.returncode == 0, f"Colony crashed: {result.stderr}"
    assert "MARS BARN" in result.stdout, f"No output: {result.stdout[:200]}"

def test_colony_has_survivors():
    """At least one colony should survive 1 sol."""
    result = subprocess.run(
        [sys.executable, str(SRC / "main.py")],
        capture_output=True, text=True, timeout=30
    )
    assert result.returncode == 0
    assert "✓" in result.stdout, "No surviving colonies after 1 sol"
