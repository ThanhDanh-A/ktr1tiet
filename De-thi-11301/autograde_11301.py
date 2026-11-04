"""Bo tu cham tham khao cho de Python ma 11301.

- Dung rubric dap an trong PDF de lam co so chia diem.
- Chay cac file Cau1.py ... Cau5.py trong thu muc bai lam.
- Hien ✅ neu tieu chi dat, ❌ neu chua dat; tinh diem du kien /10.

Day la bo tu kiem tra cuc bo, khong phai he thong cham chinh thuc cua giang vien.
"""

from __future__ import annotations

import ast
import os
import re
import subprocess
import sys
import unicodedata
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parent
REQUIRED_FILES = [f"Cau{i}.py" for i in range(1, 6)]


@dataclass
class CheckResult:
    label: str
    max_score: float
    passed: bool
    detail: str


def normalize(text: str) -> str:
    """Normalize Unicode and remove whitespace for robust output checks."""
    text = unicodedata.normalize("NFC", text).casefold()
    return "".join(text.split())


def find_submission_dir() -> Path | None:
    """Find HOTEN_MSSV or a renamed student folder containing all five files."""
    preferred = ROOT / "HOTEN_MSSV"
    if preferred.is_dir() and all((preferred / name).is_file() for name in REQUIRED_FILES):
        return preferred

    candidates = []
    for child in ROOT.iterdir():
        if child.is_dir() and child.name not in {".vscode", "__pycache__"}:
            if all((child / name).is_file() for name in REQUIRED_FILES):
                candidates.append(child)
    if len(candidates) == 1:
        return candidates[0]
    return None


def run_program(folder: Path, filename: str, input_data: str = "") -> tuple[str, str | None]:
    """Run one student program with controlled stdin and UTF-8 output."""
    path = folder / filename
    if not path.is_file():
        return "", f"Khong tim thay file {path.name}"

    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    try:
        completed = subprocess.run(
            [sys.executable, str(path)],
            input=input_data,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=ROOT,
            env=env,
            timeout=5,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return "", "Chuong trinh chay qua 5 giay"
    except OSError as exc:
        return "", f"Khong the chay file: {exc}"

    if completed.returncode != 0:
        error = completed.stderr.strip() or f"Ma ket thuc {completed.returncode}"
        return completed.stdout, error
    return completed.stdout, None


def parse_ast(folder: Path, filename: str) -> ast.Module | None:
    path = folder / filename
    try:
        return ast.parse(path.read_text(encoding="utf-8"))
    except (OSError, SyntaxError, UnicodeDecodeError):
        return None


def has_function(folder: Path, filename: str, function_name: str) -> bool:
    tree = parse_ast(folder, filename)
    return bool(tree and any(isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == function_name for node in tree.body))


def result(label: str, score: float, passed: bool, detail: str) -> CheckResult:
    return CheckResult(label, score, passed, detail)


def check_c1a(folder: Path) -> CheckResult:
    score = 0.5
    output, error = run_program(folder, "Cau1.py", "0\n1501\n635\n")
    if error:
        return result("Câu 1a - Kiểm tra n trong [1;1500]", score, False, error)
    valid = (
        output.count("Nhập lại giá trị") >= 2
        and "Số lượng chữ số lẻ là" in output
        and re.search(r"Số lượng chữ số lẻ là\s*:?\s*2", output) is not None
    )
    detail = "Đã yêu cầu nhập lại với 0 và 1501, sau đó nhận n=635." if valid else "Chưa thấy chương trình từ chối 0/1501 và nhận lại giá trị hợp lệ."
    return result("Câu 1a - Kiểm tra n trong [1;1500]", score, valid, detail)


def check_c1b(folder: Path) -> CheckResult:
    score = 0.75
    if not has_function(folder, "Cau1.py", "DemChuSoLe"):
        return result("Câu 1b - Hàm DemChuSoLe", score, False, "Thiếu hàm DemChuSoLe(n).")
    out1, err1 = run_program(folder, "Cau1.py", "635\n")
    out2, err2 = run_program(folder, "Cau1.py", "1248\n")
    if err1 or err2:
        return result("Câu 1b - Hàm DemChuSoLe", score, False, err1 or err2 or "Lỗi chạy chương trình")
    ok = bool(re.search(r"Số lượng chữ số lẻ là\s*:?\s*2", out1)) and bool(
        re.search(r"Số lượng chữ số lẻ là\s*:?\s*1", out2)
    )
    detail = "Hàm đếm đúng với 635 → 2 và 1248 → 1." if ok else "Kết quả đếm chữ số lẻ chưa đúng với bộ thử 635 và 1248."
    return result("Câu 1b - Hàm DemChuSoLe", score, ok, detail)


def extract_s_value(output: str) -> float | None:
    match = re.search(r"S\s*=\s*(-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)", output)
    if not match:
        return None
    try:
        return float(match.group(1))
    except ValueError:
        return None


def check_c1c(folder: Path) -> CheckResult:
    score = 0.75
    if not has_function(folder, "Cau1.py", "S"):
        return result("Câu 1c - Hàm tính S", score, False, "Thiếu hàm S(n).")
    output, error = run_program(folder, "Cau1.py", "3\n")
    if error:
        return result("Câu 1c - Hàm tính S", score, False, error)
    actual = extract_s_value(output)
    expected = 0.5 + 0.25 + (1 / 6)
    ok = actual is not None and abs(actual - expected) < 1e-8
    detail = f"S(3) = {actual:.8f}, đúng với 1/2 + 1/4 + 1/6." if ok and actual is not None else "Giá trị S(3) chưa khớp 1/2 + 1/4 + 1/6."
    return result("Câu 1c - Hàm tính S", score, ok, detail)


def check_c2a(folder: Path) -> CheckResult:
    score = 0.75
    output, error = run_program(folder, "Cau2.py", "aBCd1\n")
    if error:
        return result("Câu 2a - Đếm chữ hoa", score, False, error)
    ok = re.search(r"Số ký tự chữ hoa\s*:?\s*2", output) is not None
    detail = "Đếm đúng 2 ký tự viết hoa trong aBCd1." if ok else "Kết quả đếm ký tự chữ hoa chưa đúng."
    return result("Câu 2a - Đếm chữ hoa", score, ok, detail)


def check_c2b(folder: Path) -> CheckResult:
    score = 0.5
    if not has_function(folder, "Cau2.py", "DoiXung"):
        return result("Câu 2b - Kiểm tra chuỗi đối xứng", score, False, "Thiếu hàm DoiXung(s) theo đáp án tham khảo.")
    out1, err1 = run_program(folder, "Cau2.py", "level\n")
    out2, err2 = run_program(folder, "Cau2.py", "Python\n")
    if err1 or err2:
        return result("Câu 2b - Kiểm tra chuỗi đối xứng", score, False, err1 or err2 or "Lỗi chạy chương trình")
    ok = "chuỗiđốixứng." in normalize(out1) and "chuỗikhôngđốixứng." in normalize(out2)
    detail = "Nhận đúng cả chuỗi đối xứng (level) và không đối xứng (Python)." if ok else "Chưa phân biệt đúng hai trường hợp đối xứng/không đối xứng."
    return result("Câu 2b - Kiểm tra chuỗi đối xứng", score, ok, detail)


def check_c2c(folder: Path) -> CheckResult:
    score = 0.75
    output, error = run_program(folder, "Cau2.py", "a1b2c3\n")
    if error:
        return result("Câu 2c - Tính tổng chữ số", score, False, error)
    ok = re.search(r"Tổng các chữ số trong chuỗi\s*:?\s*6", output) is not None
    detail = "Tính đúng 1 + 2 + 3 = 6." if ok else "Tổng các chữ số chưa đúng với chuỗi a1b2c3."
    return result("Câu 2c - Tính tổng chữ số", score, ok, detail)


def c3_input() -> str:
    return "5\n-2\n8\n5\n0\n5\n"


def check_c3a(folder: Path) -> CheckResult:
    score = 0.75
    output, error = run_program(folder, "Cau3.py", c3_input())
    if error:
        return result("Câu 3a - Nhập list đến khi gặp 0", score, False, error)
    ok = "Danh sách vừa nhập: [5, -2, 8, 5]" in output and "0]" not in output
    detail = "Dừng khi nhập 0 và in list [5, -2, 8, 5]." if ok else "Danh sách chưa được dừng đúng tại 0 hoặc in chưa đúng."
    return result("Câu 3a - Nhập list đến khi gặp 0", score, ok, detail)


def check_c3b(folder: Path) -> CheckResult:
    score = 0.75
    output, error = run_program(folder, "Cau3.py", c3_input())
    if error:
        return result("Câu 3b - Tổng số dương chẵn", score, False, error)
    ok = re.search(r"Tổng các số dương chẵn trong danh sách\s*:?\s*8", output) is not None
    detail = "Tổng đúng: chỉ lấy 8; bỏ qua -2 và các số lẻ." if ok else "Tổng số dương chẵn chưa đúng với list thử."
    return result("Câu 3b - Tổng số dương chẵn", score, ok, detail)


def check_c3c(folder: Path) -> CheckResult:
    score = 0.5
    output, error = run_program(folder, "Cau3.py", c3_input())
    if error:
        return result("Câu 3c - Đếm số lần xuất hiện của k", score, False, error)
    ok = re.search(r"Số lần xuất hiện của\s*5\s*là\s*:?\s*2", output) is not None
    detail = "Đếm đúng k=5 xuất hiện 2 lần." if ok else "Số lần xuất hiện của k chưa đúng."
    return result("Câu 3c - Đếm số lần xuất hiện của k", score, ok, detail)


def c4_run(folder: Path, delete_code: str) -> tuple[str, str | None]:
    current_year = datetime.now().year
    data = (
        f"0\n1\nB001\nPython Co Ban\nNguyen Van A\nNXB Tre\n{current_year + 1}\n"
        f"{current_year - 1}\n{delete_code}\n"
    )
    return run_program(folder, "Cau4.py", data)


def check_c4a(folder: Path) -> CheckResult:
    score = 1.5
    output, error = c4_run(folder, "KHONG_CO_MA_NAY")
    if error:
        return result("Câu 4a - Nhập và lưu sách vào dictionary", score, False, error)
    required = [
        "Nhập lại số lượng sách",
        "Năm xuất bản không hợp lệ",
        "B001",
        "Python Co Ban",
        "Nguyen Van A",
        "NXB Tre",
        str(datetime.now().year - 1),
    ]
    missing = [item for item in required if normalize(item) not in normalize(output)]
    expected_record = ["Python Co Ban", "Nguyen Van A", "NXB Tre", datetime.now().year - 1]
    dictionary_ok = False
    for line in output.splitlines():
        try:
            value = ast.literal_eval(line.strip())
        except (ValueError, SyntaxError):
            continue
        if isinstance(value, dict) and value.get("B001") == expected_record:
            dictionary_ok = True
            break
    ok = not missing and dictionary_ok
    if not dictionary_ok:
        missing.append("dictionary chưa lưu đúng cấu trúc mã sách -> [tên, tác giả, NXB, năm]")
    detail = "Đã thử n<=0, năm tương lai và lưu đủ thông tin sách vào dictionary." if ok else "Thiếu/không đúng: " + ", ".join(missing)
    return result("Câu 4a - Nhập và lưu sách vào dictionary", score, ok, detail)


def check_c4b(folder: Path) -> CheckResult:
    score = 0.5
    out_found, err1 = c4_run(folder, "B001")
    out_missing, err2 = c4_run(folder, "KHONG_CO_MA_NAY")
    if err1 or err2:
        return result("Câu 4b - Xóa sách theo mã", score, False, err1 or err2 or "Lỗi chạy chương trình")
    found_ok = normalize("Cuốn sách có mã số B001 đã được xóa.") in normalize(out_found)
    missing_ok = normalize("Không tìm thấy cuốn sách cần xóa.") in normalize(out_missing)
    ok = found_ok and missing_ok
    detail = "Xóa đúng khi mã tồn tại và thông báo đúng khi mã không tồn tại." if ok else "Chưa xử lý đúng cả hai trường hợp mã sách có/không tồn tại."
    return result("Câu 4b - Xóa sách theo mã", score, ok, detail)


def check_c5a(folder: Path) -> CheckResult:
    score = 1.0
    tree = parse_ast(folder, "Cau5.py")
    if tree is None:
        return result("Câu 5a - Lớp DienThoai", score, False, "Không đọc được cú pháp Cau5.py.")
    cls = next((node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == "DienThoai"), None)
    if cls is None:
        return result("Câu 5a - Lớp DienThoai", score, False, "Thiếu class DienThoai.")
    methods = {node.name: node for node in cls.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))}
    init = methods.get("__init__")
    display = methods.get("thongtindienthoai")
    required_attrs = {"MaMay", "TenMay", "HangSanXuat", "DungLuongPin", "GiaBan"}
    assigned_attrs = set()
    if init:
        for node in ast.walk(init):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name) and target.value.id == "self":
                        assigned_attrs.add(target.attr)
    missing_attrs = sorted(required_attrs - assigned_attrs)
    required_parameters = ["self", "MaMay", "TenMay", "HangSanXuat", "DungLuongPin", "GiaBan"]
    actual_parameters = [arg.arg for arg in init.args.args] if init else []
    signature_ok = actual_parameters == required_parameters
    ok = init is not None and display is not None and not missing_attrs and signature_ok
    if not signature_ok:
        missing_attrs.append("tham số __init__ chưa đúng thứ tự/tên theo đề")
    detail = "Có class, __init__, phương thức hiển thị và đủ 5 thuộc tính." if ok else "Thiếu __init__/thongtindienthoai hoặc thuộc tính: " + ", ".join(missing_attrs)
    return result("Câu 5a - Lớp DienThoai", score, ok, detail)


def _literal_call_args(node: ast.AST) -> list[object] | None:
    if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Name) or node.func.id != "DienThoai":
        return None
    values = []
    for arg in node.args:
        if not isinstance(arg, ast.Constant):
            return None
        values.append(arg.value)
    return values


def check_c5b(folder: Path) -> CheckResult:
    score = 1.0
    tree = parse_ast(folder, "Cau5.py")
    if tree is None:
        return result("Câu 5b - Tạo hai đối tượng điện thoại", score, False, "Không đọc được cú pháp Cau5.py.")

    wanted = {
        "DT1": ["DT01", "iPhone 15 Pro", "Apple", 3274, 28990000],
        "DT2": ["DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000],
    }
    found: dict[str, list[object]] = {}
    called_methods: set[str] = set()
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in wanted:
                    args = _literal_call_args(node.value)
                    if args is not None:
                        found[target.id] = args
        elif isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            call = node.value
            if isinstance(call.func, ast.Attribute) and call.func.attr == "thongtindienthoai" and isinstance(call.func.value, ast.Name):
                called_methods.add(call.func.value.id)

    structure_ok = all(found.get(name) == values for name, values in wanted.items()) and {"DT1", "DT2"}.issubset(called_methods)
    output, error = run_program(folder, "Cau5.py")
    if error:
        return result("Câu 5b - Tạo hai đối tượng điện thoại", score, False, error)
    required_output = [
        "Mã máy: DT01", "Tên máy: iPhone 15 Pro", "Hãng sản xuất: Apple",
        "Dung lượng pin: 3274", "Giá bán: 28990000",
        "Mã máy: DT02", "Tên máy: Galaxy S24 Ultra", "Hãng sản xuất: Samsung",
        "Dung lượng pin: 5000", "Giá bán: 29990000",
    ]
    output_ok = all(normalize(item) in normalize(output) for item in required_output)
    ok = structure_ok and output_ok
    detail = "Tạo đúng DT1/DT2 theo dữ liệu đề và gọi phương thức để in đủ thông tin." if ok else "Đối tượng, tham số khởi tạo, lời gọi phương thức hoặc output chưa khớp đề."
    return result("Câu 5b - Tạo hai đối tượng điện thoại", score, ok, detail)


def run_grader() -> int:
    folder = find_submission_dir()
    if folder is None:
        print("❌ Không tìm thấy thư mục bài làm có đủ Cau1.py đến Cau5.py.")
        print("   Hãy để 5 file trong HOTEN_MSSV hoặc trong một thư mục tên riêng của em.")
        return 2

    checks: list[Callable[[Path], CheckResult]] = [
        check_c1a, check_c1b, check_c1c,
        check_c2a, check_c2b, check_c2c,
        check_c3a, check_c3b, check_c3c,
        check_c4a, check_c4b,
        check_c5a, check_c5b,
    ]

    print("=" * 72)
    print("TỰ CHẤM BÀI PYTHON - MÃ ĐỀ 11301")
    print(f"Thư mục bài làm: {folder.name}")
    print("Điểm tự kiểm tra theo rubric tham khảo trong PDF - không phải điểm chính thức.")
    print("=" * 72)

    results = [check(folder) for check in checks]
    total = 0.0
    maximum = 0.0
    for item in results:
        mark = "✅" if item.passed else "❌"
        earned = item.max_score if item.passed else 0.0
        total += earned
        maximum += item.max_score
        print(f"{mark} {item.label:<48} {earned:.2f}/{item.max_score:.2f}")
        if not item.passed:
            print(f"   └─ {item.detail}")

    print("-" * 72)
    print(f"KẾT QUẢ: {total:.2f}/{maximum:.2f} điểm tự kiểm tra")
    print(f"ĐẠT: {sum(item.passed for item in results)}/{len(results)} tiêu chí")
    if total == maximum:
        print("🎉 Tất cả tiêu chí tự kiểm tra đều đạt. Em vẫn cần tự đọc lại đề và code trước khi nộp.")
    else:
        print("⚠️ Có tiêu chí chưa đạt. Xem ghi chú dưới dấu ❌, sửa file rồi chạy lại.")
    print("Lưu ý: Đây là bộ tự chấm tham khảo theo đáp án trong PDF; giảng viên là người chấm điểm chính thức.")
    print("=" * 72)
    return 0 if total == maximum else 1


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except (OSError, ValueError):
            pass
    raise SystemExit(run_grader())
