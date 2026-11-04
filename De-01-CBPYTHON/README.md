# Đề số 01 - CBPYTHON 🐍

Bộ bài giải cho **Đề số 01 - CBPYTHON** và bộ chấm tự động chạy trực tiếp trong Visual Studio Code.

## 1. Chuẩn bị một lần

1. Cài Python 3.9 trở lên. Trên Windows, nên chọn **Add Python to PATH** khi cài.
2. Cài Visual Studio Code.
3. Trong VS Code → Extensions, cài extension **Python** của Microsoft (`ms-python.python`).
4. Chọn **File → Open Folder** và mở đúng thư mục **De-01-CBPYTHON** (thư mục có file `autograde_de1_v2.py`).
5. Nhấn `Ctrl + Shift + P`, chọn **Python: Select Interpreter**, rồi chọn phiên bản Python đã cài.

## 2. Chấm điểm cả đề bằng một phím tắt

1. Nhấn **Ctrl + Shift + B**.
2. Terminal của VS Code sẽ mở và hỏi họ tên, MSSV, số máy.
3. Nhập thông tin; nếu không có số máy thì nhấn Enter.
4. Xem PASS/FAIL từng test và dòng **TONG DIEM** khi chương trình chạy xong.

Task đã được cấu hình trong `.vscode/tasks.json` và sử dụng đúng interpreter em chọn trong VS Code. Terminal được mở ở chế độ nhận nhập liệu để em điền thông tin.

## 3. Chấm điểm bằng Terminal nếu phím tắt không chạy

Chọn **Terminal → New Terminal**, bảo đảm terminal đang ở thư mục `De-01-CBPYTHON`, rồi chạy:

```powershell
python autograde_de1_v2.py
```

Nếu Windows không nhận lệnh `python`, thử:

```powershell
py autograde_de1_v2.py
```

Trên macOS/Linux, thử:

```bash
python3 autograde_de1_v2.py
```

## 4. Chạy riêng một câu

Mở file trong `submissions_de1`, sau đó bấm **Run Python File**. Cách này chỉ chạy riêng câu đó, không chấm tổng điểm. Muốn chấm cả đề, dùng `autograde_de1_v2.py`.

## 5. Các bài trong đề

| Câu | Nội dung | File |
|---|---|---|
| 1a | Kiểm tra chẵn/lẻ | `submissions_de1/Cau1a.py` |
| 1b | Nhập tên, tuổi và in lời chào | `submissions_de1/Cau1b.py` |
| 2a | Tính tổng số chẵn trong đoạn | `submissions_de1/Cau2a.py` |
| 2b | Đếm chữ số trong đoạn chuỗi | `submissions_de1/Cau2b.py` |
| 3a | Lọc phần tử kiểu chuỗi trong list | `submissions_de1/Cau3a.py` |
| 3b | Thêm, xóa và đảo list | `submissions_de1/Cau3b.py` |
| 4a | Truy cập phần tử tuple | `submissions_de1/Cau4a.py` |
| 4b | Nối và lặp tuple | `submissions_de1/Cau4b.py` |
| 5a | Đếm tần suất ký tự bằng dictionary | `submissions_de1/Cau5a.py` |
| 5b | Lọc học sinh theo điểm | `submissions_de1/Cau5b.py` |

## 6. Kiểm tra bộ chấm và bài làm

Kiểm tra logic của bộ chấm:

```bash
python -m unittest -v test_autograder.py
```

Chạy bộ tự kiểm tra 10 bài:

```bash
python kiem_thu.py
```

Hai lệnh trên là kiểm tra phụ. Để lấy điểm theo test của đề, chạy `python autograde_de1_v2.py`.

## 7. Cấu trúc thư mục

```text
De-01-CBPYTHON/
├── .vscode/
│   ├── extensions.json
│   └── tasks.json
├── De-bai.pdf
├── README.md
├── autograde_de1_v2.py
├── test_de1.py
├── test_autograder.py
├── kiem_thu.py
└── submissions_de1/
    ├── Cau1a.py ... Cau5b.py
```

## Lưu ý về điểm số

Điểm hiển thị là kết quả chạy bộ test cục bộ trong gói tài liệu, không phải điểm chính thức trên hệ thống của giảng viên. Bộ chấm cần Python 3.9 trở lên, chỉ dùng thư viện chuẩn và không cần cài thêm package bằng pip.
