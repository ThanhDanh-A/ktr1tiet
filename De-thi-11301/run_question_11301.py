"""Run one exam question from the current student folder, even after renaming it."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

from autograde_11301 import find_submission_dir


def main() -> int:
    if len(sys.argv) != 2 or sys.argv[1] not in {"1", "2", "3", "4", "5"}:
        print("Cach dung: python run_question_11301.py [1-5]")
        return 2

    folder = find_submission_dir()
    if folder is None:
        print("Khong tim thay thu muc bai lam co du Cau1.py den Cau5.py.")
        return 2

    script = folder / f"Cau{sys.argv[1]}.py"
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    try:
        completed = subprocess.run(
            [sys.executable, str(script)],
            cwd=Path(__file__).resolve().parent,
            env=env,
            check=False,
        )
        return completed.returncode
    except OSError as exc:
        print(f"Khong the chay bai: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
