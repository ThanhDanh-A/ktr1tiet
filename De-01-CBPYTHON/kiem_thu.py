"""Kiem thu 10 bai trong de so 01 - CBPYTHON bang thu vien chuan Python."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
SUBMISSIONS = ROOT / "submissions_de1"
PYTHON = sys.executable


def run_file(filename, input_text=""):
    path = SUBMISSIONS / filename
    result = subprocess.run(
        [PYTHON, str(path)],
        input=input_text,
        text=True,
        capture_output=True,
        timeout=5,
        cwd=ROOT,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr or f"Chuong trinh {filename} ket thuc loi")
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def check(filename, cases):
    for input_text, expected in cases:
        output = run_file(filename, input_text)
        if expected(output):
            print(f"PASS  {filename}  input={input_text!r}")
        else:
            print(f"FAIL  {filename}  input={input_text!r}  output={output!r}")
            return False
    return True


def contains_line(value):
    return lambda output: any(line.endswith(value) for line in output)


def main():
    checks = [
        ("Cau1a.py", [("4\n", contains_line("Chan")), ("7\n", contains_line("Le")), ("0\n", contains_line("Chan")), ("-3\n", contains_line("Le"))]),
        ("Cau1b.py", [("An\n20\n", contains_line("Xin chao An, ban 20 tuoi.")), ("Long\n18\n", contains_line("Xin chao Long, ban 18 tuoi."))]),
        ("Cau2a.py", [("2\n10\n", contains_line("30")), ("5\n11\n", contains_line("24")), ("3\n3\n", contains_line("0")), ("-2\n2\n", contains_line("0"))]),
        ("Cau2b.py", [("abc12345\n1\n8\n", contains_line("5")), ("a1b2c3d4e5\n2\n9\n", contains_line("4")), ("abcdef\n1\n6\n", contains_line("0"))]),
        ("Cau3a.py", [("", contains_line("['apple', 'banana']"))]),
        ("Cau3b.py", [("", lambda o: len(o) == 3 and o[0] == "[100, 'apple', 3.14, 'banana', 200, None, 'orange']" and o[1] == "[100, 'apple', 'banana', 200, None, 'orange']" and o[2] == "['orange', None, 200, 'banana', 'apple', 100]")]),
        ("Cau4a.py", [("", lambda o: o == ["apple", "cherry", "coc"])]),
        ("Cau4b.py", [("", lambda o: o == ["(1, 2, 3, 4)", "(1, 2, 1, 2, 1, 2)"])]),
        ("Cau5a.py", [("", contains_line("{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}"))]),
        ("Cau5b.py", [("", contains_line("['An', 'Cuong', 'Hoa']"))]),
    ]

    passed = 0
    total = 0
    for filename, cases in checks:
        ok = check(filename, cases)
        passed += int(ok)
        total += 1

    print("\nKet qua: {}/{} bai dat kiem thu.".format(passed, total))
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
