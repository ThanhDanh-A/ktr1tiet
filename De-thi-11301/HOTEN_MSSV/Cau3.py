# CAU 3 (2.0 diem): Tao danh sach so nguyen, nhap 0 de ket thuc.

# a. Nhap cac phan tu vao danh sach.
danh_sach = []
while True:
    x = int(input("Nhập danh sách: "))
    if x == 0:
        break
    danh_sach.append(x)

print("Danh sách vừa nhập:", danh_sach)

# b. Tinh tong cac so duong chan co trong danh sách.
tong = 0
for i in danh_sach:
    if (i > 0) and (i % 2 == 0):
        tong += i

if tong != 0:
    print("Tổng các số dương chẵn trong danh sách:", tong)
else:
    print("Không có số dương chẵn trong danh sách.")

# c. Dem so lan xuat hien cua phan tu k.
k = int(input("Nhập k: "))
dem = 0
for i in danh_sach:
    if i == k:
        dem += 1

if dem == 0:
    print("Không có phần tử", k, "trong danh sách")
else:
    print("Số lần xuất hiện của", k, "là:", dem)
