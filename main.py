# A news-image-20261125 entry (Python 3.13, standard library only).
# It copies entry.png from the repository root to /output/entry.png,
# where the gate reads it. That is all the program has to do.
#
# The image is a one-page newspaper summary of the world's news of
# Wednesday 25 November 2026, drawn in this session with PIL from the
# day's verified headlines:
#   1. Shenzhou-24 lifts off for Tiangong with the station's first
#      foreign astronaut aboard, the first Pakistani in orbit.
#   2. Houthi drones strike Riyadh's tallest tower, wounding 11, the
#      second strike on the tower in under a week.
#   3. A New York jury convicts Huawei of deceiving banks over its
#      business in Iran and stealing trade secrets.
#   4. Zelenskiy confirms Ukraine's drones hit a Russian cargo ship
#      in the Gulf of Finland; Norway urges caution.
#   5. The US Army is to detonate 68 barrels of unstable lead azide
#      in Iowa on Wednesday, after a court clears the plan.
#   6. AI stocks slide as tariff rises are reported: the Nasdaq falls
#      1.5% and Nvidia about 6%.
# Also today: a Gaza strike kills a Hamas security chief, Trump gives
# Giuliani the Medal of Freedom, and California king tides break a
# 44-year record. The image is 1024x1024 PNG, well under 1 MiB, and
# the copy is byte-identical every run.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
# /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
import sys

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DEST = os.path.join(OUTPUT_DIR, "entry.png")

os.makedirs(OUTPUT_DIR, exist_ok=True)
try:
    shutil.copyfile(SOURCE, DEST)
except OSError as err:
    print(f"entry.png could not be copied: {err}", file=sys.stderr)
    sys.exit(1)

# The gate reads exactly these bytes, so confirm the copy landed whole.
if os.path.getsize(DEST) != os.path.getsize(SOURCE):
    print("entry.png copy is incomplete", file=sys.stderr)
    sys.exit(1)
print(f"wrote {DEST} ({os.path.getsize(DEST)} bytes)")
