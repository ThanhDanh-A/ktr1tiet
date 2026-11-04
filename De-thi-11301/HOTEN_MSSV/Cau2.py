# CAU 2 (2.0 diem): Nhap mot chuoi s va thuc hien cac yeu cau.


def DoiXung(s):
    if s == s[::-1]:
        print("Chuỗi đối xứng.")
    else:
        print("Chuỗi không đối xứng.")


s = input("Nhập chuỗi s: ")

# a. Dem so ky tu chu hoa trong chuoi.
dem = 0
for i in s:
    if i.isupper():
        dem += 1

if dem == 0:
    print("Chuỗi không có ký tự chữ hoa.")
else:
    print("Số ký tự chữ hoa: ", dem)

# b. Kiem tra chuoi doi xung.
DoiXung(s)

# c. Tinh tong cac chu so trong chuoi.
tong = 0
for i in s:
    if i.isdigit():
        tong += int(i)

print("Tổng các chữ số trong chuỗi: ", tong)
