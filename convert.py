# Simple parser the call the hrm converter.
# Open JDK jre is needed, not the headless one
import os
import subprocess
from pathlib import Path

IN = "/home/chris/Downloads/in"
OUT = "/home/chris/Downloads/out"
JWHGT = "/home/chris/JWHGT"

for f in [f for f in os.listdir(IN) if f.lower().endswith(".hrm")]:
    in_name = f
    out_name = f"{Path(f).stem}.tcx"

    out_path = os.path.join(OUT, out_name)
    in_path = os.path.join(IN, in_name)

    if os.path.exists(out_path):
        os.remove(out_path)

    result = subprocess.run(
        [
            "java",
            "-jar",
            os.path.join(JWHGT, "JWHGT.jar"),
            "-con",
            "-exts",
            "ex",
            "-exsd",
            "hrec",
            "-ifhrm",
            in_path,
            "-of",
            out_path,
        ],
        capture_output=True,
    )

    if result.returncode == 0:
        print(f"OK  {in_name} --> {out_name}")
    else:
        print(f"ERR {in_name}: ret={result.returncode} - {result.stdout}")
