# Cau 3a: Tao danh sach moi chi gom cac phan tu kieu chuoi

lst = [100, "apple", 3.14, "banana", 200, None]

danh_sach_chuoi = []
for phan_tu in lst:
    if isinstance(phan_tu, str):
        danh_sach_chuoi.append(phan_tu)

print(danh_sach_chuoi)
