# Đề số 01 - CBPYTHON 🐍

Bài giải cho **Đề số 01 - CBPYTHON** cùng bộ chấm tự động cục bộ dựa trên các test case trong tài liệu giảng viên cung cấp.

## Chấm tự động trong VS Code

1. Giải nén repository hoặc tải ZIP về máy.
2. Mở VS Code → **File → Open Folder** → chọn trực tiếp thư mục `De-01-CBPYTHON`.
3. Mở **Terminal → New Terminal**.
4. Chạy lệnh:

   ```bash
   python autograde_de1_v2.py
   ```

5. Nhập họ tên, MSSV và số máy (có thể nhấn Enter để bỏ qua số máy).
6. Chương trình tự chạy test cho 10 file và in PASS/FAIL cùng tổng điểm trên thang 10.

Nếu máy dùng lệnh `py` thay cho `python`, chạy:

```bash
py autograde_de1_v2.py
```

**Phím tắt trong VS Code:** nhấn **Ctrl + Shift + B** để chạy task `Chấm điểm tự động - Đề 01 CBPYTHON` đã cấu hình sẵn.

## Chạy riêng từng câu

Mở thư mục `submissions_de1`, chọn `Cau1a.py`, `Cau1b.py`, ... rồi nhấn **Run Python File**. Cách này chỉ chạy một bài riêng lẻ; muốn chấm cả đề thì chạy `autograde_de1_v2.py`.

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

## Các file kiểm tra

- `autograde_de1_v2.py`: bộ chấm, tự chạy chương trình của từng câu với dữ liệu vào và đối chiếu đầu ra.
- `test_de1.py`: bộ dữ liệu test theo tài liệu thầy gửi, đã chỉnh lại phần chú thích cho khớp PDF.
- `test_autograder.py`: kiểm tra chính logic chấm để bảo đảm thiếu một dòng kết quả sẽ không được tính PASS.
- `kiem_thu.py`: bộ tự kiểm tra phụ, in PASS/FAIL cho từng bài.

Bộ chấm chỉ dùng thư viện chuẩn của Python, không cần `pip install` thêm. Khuyến nghị Python 3.9 trở lên.

## Lưu ý về chấm điểm

Bản trước có lỗi khi so sánh kết quả: nếu một test mong đợi nhiều dòng, nó chỉ cần khớp một dòng là có thể được tính PASS; trường hợp kết quả mong đợi là một chuỗi cũng bị duyệt từng ký tự. Bản hiện tại đã sửa để:

- Chuỗi mong đợi phải khớp cả cụm nội dung.
- Danh sách nhiều kết quả phải khớp **đầy đủ từng dòng** và không dùng một dòng output để tính cho nhiều kết quả.
- Dictionary được phân tích và so sánh giá trị thực tế.

**Điểm hiển thị là kết quả của bộ test cục bộ trong gói tài liệu, không phải xác nhận điểm chính thức trên hệ thống của giảng viên.**

Câu 1a trong PDF ghi “số thực” nhưng chẵn/lẻ chỉ xác định rõ cho số nguyên. Bài làm xử lý các số nguyên và số thực có phần thập phân bằng 0; với số thập phân không nguyên, bài đưa vào nhánh `Le` theo cách diễn giải của đề kiểm thử.
