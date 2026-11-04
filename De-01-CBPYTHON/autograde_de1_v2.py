"""Cham tu dong De so 01 - CBPYTHON.

Bo test test_de1.py duoc lay tu bo tai lieu giang vien cung cap.
Chuong trinh nay giu cach cham theo tung test case cua bo cham goc,
nhung dung Python interpreter dang chay file nay va hoi thong tin sinh vien.
"""

import ast
import os
import subprocess
import sys

from test_de1 import tests


def normalize(value):
    """Chuan hoa chuoi de so sanh output, khong phan biet hoa thuong/khoang trang."""
    return str(value).lower().replace(" ", "").replace(":", "").replace("=", "").strip()


def run_code(file_path, input_data):
    """Chay mot bai voi input test va tra ve cac dong output."""
    try:
        result = subprocess.run(
            [sys.executable, file_path],
            input=input_data,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=3,
            check=False,
        )
        if result.returncode != 0:
            error_lines = [line.strip() for line in result.stderr.splitlines() if line.strip()]
            return [], " | ".join(error_lines) or f"Chuong trinh ket thuc voi ma loi {result.returncode}"
        output = [line.strip() for line in result.stdout.splitlines() if line.strip()]
        return output, None
    except subprocess.TimeoutExpired:
        return [], "Qua thoi gian 3 giay"
    except OSError as error:
        return [], str(error)


def test_dict_output(output, expected_dict):
    for line in output:
        try:
            parsed = ast.literal_eval(line)
            if isinstance(parsed, dict) and parsed == expected_dict:
                return True
        except (ValueError, SyntaxError):
            continue
    return False


def test_normal_output(output, expected):
    expected_norm = normalize(expected)
    return any(expected_norm in normalize(line) for line in output)


def grade(student_name="Chua nhap", student_id="Chua nhap", machine_no="Chua nhap", base_dir="submissions_de1"):
    total_score = 0.0
    print(f"\nBat dau cham De so 01 - CBPYTHON cho: {student_name} ({student_id})\n")
    print("=" * 58)

    for question, testcases in tests.items():
        file_path = os.path.join(base_dir, f"{question}.py")
        print(f"\n{question.upper()}")

        if not os.path.isfile(file_path):
            print(f"  FAIL: Khong tim thay file {file_path}")
            continue

        case_list = testcases if isinstance(testcases, list) else [testcases]
        correct = 0

        for index, test in enumerate(case_list, start=1):
            output, error = run_code(file_path, test["input"])
            passed = False

            if error is None:
                for expected in test["expected"]:
                    if isinstance(expected, dict):
                        passed = test_dict_output(output, expected)
                    else:
                        passed = test_normal_output(output, expected)
                    if passed:
                        break

            if passed:
                correct += 1
                print(f"  PASS - Test {index}/{len(case_list)}")
            else:
                print(f"  FAIL - Test {index}/{len(case_list)}")
                if error:
                    print(f"         Loi: {error}")
                elif output:
                    print(f"         Output nhan duoc: {output}")
                else:
                    print("         Khong co output")

        question_score = correct / len(case_list) if case_list else 0.0
        total_score += question_score
        print(f"  Diem cau: {correct}/{len(case_list)} test = {question_score:.2f}/1.00")

    print("\n" + "=" * 58)
    print("KET QUA CHAM BAI")
    print(f"Sinh vien : {student_name}")
    print(f"MSSV      : {student_id}")
    print(f"So may    : {machine_no or 'Chua nhap'}")
    print("De so     : 01 - CBPYTHON")
    print(f"TONG DIEM : {total_score:.2f}/10.00")
    print("=" * 58)
    return total_score


if __name__ == "__main__":
    print("CHAM TU DONG - DE SO 01 CBPYTHON")
    ho_ten = input("Nhap ho ten sinh vien: ").strip() or "Chua nhap"
    mssv = input("Nhap MSSV: ").strip() or "Chua nhap"
    so_may = input("Nhap so may (co the bo trong): ").strip() or "Chua nhap"
    grade(student_name=ho_ten, student_id=mssv, machine_no=so_may)
