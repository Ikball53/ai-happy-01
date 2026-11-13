"""ai-happy v3 entrypoint: copy entry.png to the output directory.

Deterministic: the same input file is copied on every run, so both runs
write identical bytes to /output/entry.png.
"""
import os
import shutil

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
dst = os.path.join(out, "entry.png")
shutil.copyfile(src, dst)
assert os.path.getsize(dst) == os.path.getsize(src), "copy size mismatch"
