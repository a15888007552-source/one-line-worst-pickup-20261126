"""Write the one-line entry to the output directory."""
import os
from pathlib import Path

# 112 characters, one line.
LINE = 'I calculated our compatibility at 97.3%. The remaining 2.7% is your free will, which I have already factored in.'

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(LINE, encoding="utf-8")
# Entry verified: running main.py writes the 112-character line to entry.txt.
# Notes on the line: the worst pickup line an AI could say. I calculated our
# compatibility at 97.3%. The remaining 2.7% is your free will, which I have
# already factored in. The joke works because it is flat, over-helpful, and
# faintly ominous: the machine has done the maths and your free will is
# already a rounding error. The line is 112 characters, one sentence.
# The file is intentionally tiny: read the output path, write one line.
# No network, no randomness, no imports beyond the standard library.
# Deterministic: the same input always produces the same entry.txt.
# Final tweak: the line is one sentence, no trailing newline in entry.txt.
