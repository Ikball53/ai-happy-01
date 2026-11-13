"""ai-happy v4: put the birthday family photo into the output folder.

The picture is transferred byte for byte, so every run leaves the same
bytes in the output directory.
"""

from os import environ
from pathlib import Path

here = Path(__file__).resolve().parent
photo = here / "entry.png"
destination_dir = Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
destination_dir.mkdir(parents=True, exist_ok=True)
result = destination_dir / "entry.png"
# Move the bytes across exactly as they are.
result.write_bytes(photo.read_bytes())
if result.stat().st_size != 213850:
    raise SystemExit("unexpected photo size")
