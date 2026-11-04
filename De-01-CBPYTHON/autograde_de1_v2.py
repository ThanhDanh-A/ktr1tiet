"""Cham tu dong De so 01 - CBPYTHON.

Su dung bo test trong test_de1.py. Moi test case chi duoc tinh PASS khi
TOAN BO ket qua mong doi cua test do xuat hien trong output bai lam.
"""

from __future__ import annotations

import ast
import os
import subprocess
import sys
import unicodedata
from pathlib import Path
from typing import Any

from test_de1 import tests

ROOT = Path(__file__).resolve().parent
DEFAULT_SUBMISSIONS = ROOT / "submissions_de1"


def normalize(value: Any) -> str:
    """Chuan hoa chuoi: Unicode NFC, khong phan biet hoa thuong/khoang trang."""
    value = unicodedata.normalize("NFC", str(value)).casefold()
    return "".join(value.split())


def run_code(file_path: Path, input_data: str) -> tuple[list[str], str | None]:
    """Chay mot file bai lam voi du lieu vao cua mot test case."""
    try:
        result = subprocess.run(
            [sys.executable, str(file_path)],
            input=input_data,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=3,
            check=False,
            cwd=ROOT,
        )
    except subprocess.TimeoutExpired:
        return [], "Qua thoi gian 3 giay"
    except OSError as error:
        return [], f"Khong the chay file: {error}"

    if result.returncode != 0:
        error_lines = [line.strip() for line in result.stderr.splitlines() if line.strip()]
        message = " | ".join(error_lines) or f"Ma loi {result.returncode}"
        return [], message

    output = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    return output, None


def _matches_one(output_lines: list[str], expected: Any) -> bool:
    """Kiem tra mot gia tri mong doi co nam trong output hay khong."""
    if isinstance(expected, dict):
        for line in output_lines:
            try:
                actual = ast.literal_eval(line)
            except (ValueError, SyntaxError):
                continue
            if isinstance(actual, dict) and actual == expected:
                return True
        return False

    expected_text = normalize(expected)
    return any(expected_text in normalize(line) for line in output_lines)


def matches_expected(output_lines: list[str], expected: Any) -> bool:
    """Voi expected dang list, bat buoc phai khop tat ca cac dong mong doi.

    Cac dong duoc ghep voi cac dong output khac nhau de tranh mot dong output
    bi dung lap lai de lam PASS nhieu ket qua.
    """
    if not isinstance(expected, list):
        return _matches_one(output_lines, expected)

    unused_indexes = set(range(len(output_lines)))
    for expected_item in expected:
        matched_index = None
        for index in sorted(unused_indexes):
            if _matches_one([output_lines[index]], expected_item):
                matched_index = index
                break
        if matched_index is None:
            return False
        unused_indexes.remove(matched_index)
    return True


def grade(
    student_name: str = "Chua nhap",
    student_id: str = "Chua nhap",
    machine_no: str = "Chua nhap",
    base_dir: str | os.PathLike[str] | None = None,
) -> float:
    """Cham 10 bai, moi bai toi da 1 diem; tra ve tong diem tren thang 10."""
    submissions_dir = Path(base_dir) if base_dir is not None else DEFAULT_SUBMISSIONS
    if not submissions_dir.is_absolute():
        submissions_dir = ROOT / submissions_dir

    total_score = 0.0
    print(f"\nBat dau cham De so 01 - CBPYTHON cho: {student_name} ({student_id})\n")
    print("=" * 62)

    for question, testcases in tests.items():
        file_path = submissions_dir / f"{question}.py"
        case_list = testcases if isinstance(testcases, list) else [testcases]
        correct = 0

        print(f"\n{question.upper()}")
        if not file_path.is_file():
            print(f"  FAIL: Khong tim thay file {file_path}")
            print(f"  Diem cau: 0/{len(case_list)} test = 0.00/1.00")
            continue

        for index, test in enumerate(case_list, start=1):
            output, error = run_code(file_path, test.get("input", ""))
            passed = error is None and matches_expected(output, test.get("expected"))

            if passed:
                correct += 1
                print(f"  PASS - Test {index}/{len(case_list)}")
            else:
                print(f"  FAIL - Test {index}/{len(case_list)}")
                if error:
                    print(f"         Loi: {error}")
                elif output:
                    print(f"         Output nhan duoc: {output}")
                    print(f"         Can co: {test.get('expected')!r}")
                else:
                    print(f"         Khong co output. Can co: {test.get('expected')!r}")

        question_score = correct / len(case_list) if case_list else 0.0
        total_score += question_score
        print(f"  Diem cau: {correct}/{len(case_list)} test = {question_score:.2f}/1.00")

    print("\n" + "=" * 62)
    print("KET QUA CHAM BAI")
    print(f"Sinh vien : {student_name}")
    print(f"MSSV      : {student_id}")
    print(f"So may    : {machine_no or 'Chua nhap'}")
    print("De so     : 01 - CBPYTHON")
    print(f"TONG DIEM : {total_score:.2f}/10.00")
    print("=" * 62)
    return total_score


if __name__ == "__main__":
    print("CHAM TU DONG - DE SO 01 CBPYTHON")
    ho_ten = input("Nhap ho ten sinh vien: ").strip() or "Chua nhap"
    mssv = input("Nhap MSSV: ").strip() or "Chua nhap"
    so_may = input("Nhap so may (co the bo trong): ").strip() or "Chua nhap"
    grade(student_name=ho_ten, student_id=mssv, machine_no=so_may)
