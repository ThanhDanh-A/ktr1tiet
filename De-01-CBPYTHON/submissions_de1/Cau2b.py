# Cau 2b: Dem chu so trong mot doan cua chuoi

chuoi = input("Nhap chuoi: ")
x = int(input("Nhap vi tri x: "))
y = int(input("Nhap vi tri y: "))

# Vi tri trong de bai tinh tu 1, con chi so Python tinh tu 0.
doan_can_dem = chuoi[x - 1:y]
so_luong = 0

for ky_tu in doan_can_dem:
    if "0" <= ky_tu <= "9":
        so_luong += 1

print(so_luong)
