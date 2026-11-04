# Đề số 01 - CBPYTHON 🐍

Bài giải cho **Đề số 01 - CBPYTHON** cùng bộ chấm tự động dựa trên các test mà giảng viên cung cấp.

## Cách chấm tự động trong VS Code

**Cách 1 — chạy bằng Terminal (dễ nhất):**

1. Giải nén repository hoặc tải ZIP về máy.
2. Mở VS Code → **File → Open Folder** → chọn trực tiếp thư mục `De-01-CBPYTHON`.
3. Mở **Terminal → New Terminal**.
4. Gõ lệnh:

   ```bash
   python autograde_de1_v2.py
   ```

5. Nhập họ tên, MSSV và số máy (nếu chưa có số máy thì nhấn Enter).
6. Chương trình tự chạy các test cho 10 file và in PASS/FAIL cùng tổng điểm trên thang 10.

Nếu máy dùng lệnh `py` thay cho `python`, có thể chạy:

```bash
py autograde_de1_v2.py
```

**Cách 2 — dùng phím tắt:** nhấn **Ctrl + Shift + B** trong VS Code để chạy task chấm điểm đã cấu hình.

**Cách 3 — chạy từng câu:** mở thư mục `submissions_de1`, chọn `Cau1a.py`, `Cau1b.py`, ... rồi nhấn **Run Python File**. Cách này chỉ chạy bài riêng lẻ; muốn chấm toàn bộ đề thì chạy `autograde_de1_v2.py`.

## Các bài trong đề

| Câu | Nội dung chính | File |
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

## File chấm điểm

- `autograde_de1_v2.py`: chương trình chấm tự động, chạy từng file bài làm với dữ liệu kiểm thử và tính điểm.
- `test_de1.py`: các test case của Đề 01 được lấy từ bộ tài liệu thầy cung cấp.
- `kiem_thu.py`: bộ tự kiểm tra phụ, không thay thế bộ chấm tự động ở trên.

Bộ chấm cần Python 3.9 trở lên và chỉ dùng thư viện chuẩn, không cần `pip install` thêm.

## Lưu ý

Điểm hiển thị là kết quả của bộ test cục bộ trong tài liệu được cung cấp. Đây là kết quả tự kiểm tra trước khi nộp, không phải xác nhận điểm chính thức trên hệ thống của giảng viên.
