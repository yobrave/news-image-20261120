import os
import shutil
import sys
from pathlib import Path


def main():
    script_dir = Path(__file__).resolve().parent
    src = script_dir / "entry.png"
    if not src.is_file():
        print(f"error: source image not found: {src}", file=sys.stderr)
        return 1

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or script_dir / "out")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        print(f"error: cannot create output directory {out_dir}: {exc}", file=sys.stderr)
        return 1

    dst = out_dir / "entry.png"
    try:
        shutil.copyfile(src, dst)
    except OSError as exc:
        print(f"error: cannot copy to {dst}: {exc}", file=sys.stderr)
        return 1

    if dst.stat().st_size != src.stat().st_size:
        print(f"error: size mismatch after copy ({dst})", file=sys.stderr)
        return 1

    print(f"Copied {src} -> {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
