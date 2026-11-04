# CAU 4 (2.0 diem): Quan ly thong tin sach bang dictionary.

from datetime import datetime


# a. Nhap thong tin sach va luu vao tu dien.
n = int(input("Nhập số lượng sách (n>0): "))
while n <= 0:
    n = int(input("Nhập lại số lượng sách (n>0): "))

tu_dien = {}
nam_hien_tai = datetime.now().year

for i in range(n):
    print("Nhập thông tin sách thứ", i + 1)
    ma_so_sach = input("Nhập mã số sách: ")
    ten_sach = input("Nhập tên sách: ")
    ten_tac_gia = input("Nhập tên tác giả: ")
    nha_xuat_ban = input("Nhập nhà xuất bản: ")

    nam_xuat_ban = int(input("Nhập năm xuất bản: "))
    while nam_xuat_ban > nam_hien_tai or nam_xuat_ban <= 0:
        nam_xuat_ban = int(
            input(f"Năm xuất bản không hợp lệ, vui lòng nhập năm <= {nam_hien_tai}: ")
        )

    tu_dien[ma_so_sach] = [ten_sach, ten_tac_gia, nha_xuat_ban, nam_xuat_ban]

print("Thông tin sách trong thư viện:")
print(tu_dien)

# b. Tim va xoa sach theo ma so sach.
x = input("Nhập mã số sách cần xóa: ")
if x in tu_dien:
    del tu_dien[x]
    print(f"Cuốn sách có mã số {x} đã được xóa.")
else:
    print("Không tìm thấy cuốn sách cần xóa.")

print(tu_dien)
