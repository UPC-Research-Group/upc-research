
# Placeholder automation script
# Example: validate metadata files

import json
import sys
from pathlib import Path

def validate(file_path):
    data = json.loads(Path(file_path).read_text())
    required = ["title", "abstract", "keywords", "version", "license"]
    missing = [k for k in required if k not in data]
    if missing:
        print("Missing keys:", missing)
        sys.exit(1)
    print("Metadata is valid.")

if __name__ == "__main__":
    validate(sys.argv[1])
